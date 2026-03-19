import os
import json
import yaml
from typing import List, Optional, Dict, Any
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.core.database import get_db_connection

# Configuração de Embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def update_knowledge_base(file_path: str, metadata: Optional[Dict[str, Any]] = None):
    """
    Carrega um PDF, divide em chunks, gera embeddings e salva no banco.
    """
    if not os.path.exists(file_path):
        return {"error": f"Arquivo não encontrado: {file_path}"}

    try:
        # 1. Load
        loader = PyPDFLoader(file_path)
        docs = loader.load()

        # 2. Split
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100
        )
        chunks = text_splitter.split_documents(docs)

        # 3. Embed & Store
        conn = get_db_connection()
        cur = conn.cursor()

        for chunk in chunks:
            content = chunk.page_content
            # Gera embedding
            vector = embeddings.embed_query(content)

            # Merge metadata
            final_metadata = chunk.metadata.copy()
            if metadata:
                final_metadata.update(metadata)

            cur.execute(
                """
                INSERT INTO knowledge_base (content, embedding, metadata, source_uri)
                VALUES (%s, %s, %s, %s)
                """,
                (content, vector, json.dumps(final_metadata), file_path)
            )

        conn.commit()
        cur.close()
        conn.close()

        return {"status": "success", "chunks_processed": len(chunks)}
    except Exception as e:
        if 'conn' in locals() and conn:
            conn.rollback()
        return {"error": str(e)}

def query_knowledge_base(query: str, top_k: int = 5):
    """
    Realiza busca semântica no Vector DB.
    """
    try:
        # 1. Gera embedding da query
        query_vector = embeddings.embed_query(query)

        # 2. Busca no Postgres usando pgvector (cosine similarity)
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT content, metadata, source_uri, 1 - (embedding <=> %s::vector) as similarity
            FROM knowledge_base
            ORDER BY embedding <=> %s::vector
            LIMIT %s
            """,
            (query_vector, query_vector, top_k)
        )

        results = []
        for row in cur.fetchall():
            results.append({
                "content": row[0],
                "metadata": row[1],
                "source": row[2],
                "score": float(row[3])
            })

        cur.close()
        conn.close()

        if not results:
            return [{
                "content": "Desculpe, não encontrei informações específicas sobre isso na minha base de conhecimento atual.",
                "metadata": {"type": "fallback"},
                "source": None,
                "score": 0.0
            }]

        return results
    except Exception as e:
        return {"error": str(e)}

# IoT Catalog CRUD operations
def add_iot_product(name: str, brand: str, protocol: str, payload_yaml: str, metadata: Optional[Dict] = None):
    try:
        # Validate YAML
        yaml.safe_load(payload_yaml)

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO iot_products (name, brand, protocol, payload_yaml, metadata)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id, created_at, updated_at
            """,
            (name, brand, protocol, payload_yaml, json.dumps(metadata or {}))
        )
        row = cur.fetchone()
        product_id = row[0]
        created_at = row[1]
        updated_at = row[2]
        conn.commit()
        cur.close()
        conn.close()
        return {
            "status": "success",
            "id": product_id,
            "name": name,
            "brand": brand,
            "protocol": protocol,
            "payload_yaml": payload_yaml,
            "metadata": metadata or {},
            "created_at": created_at,
            "updated_at": updated_at
        }
    except Exception as e:
        return {"error": str(e)}

def get_iot_products():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, brand, protocol, payload_yaml, metadata, created_at, updated_at FROM iot_products ORDER BY id DESC")
        products = []
        for row in cur.fetchall():
            products.append({
                "id": row[0],
                "name": row[1],
                "brand": row[2],
                "protocol": row[3],
                "payload_yaml": row[4],
                "metadata": row[5],
                "created_at": row[6],
                "updated_at": row[7]
            })
        cur.close()
        conn.close()
        return products
    except Exception as e:
        return {"error": str(e)}

def update_iot_product(product_id: int, name: Optional[str] = None, brand: Optional[str] = None, protocol: Optional[str] = None, payload_yaml: Optional[str] = None, metadata: Optional[Dict] = None):
    try:
        updates = []
        params = []
        if name:
            updates.append("name = %s")
            params.append(name)
        if brand:
            updates.append("brand = %s")
            params.append(brand)
        if protocol:
            updates.append("protocol = %s")
            params.append(protocol)
        if payload_yaml:
            yaml.safe_load(payload_yaml)
            updates.append("payload_yaml = %s")
            params.append(payload_yaml)
        if metadata:
            updates.append("metadata = %s")
            params.append(json.dumps(metadata))

        if not updates:
            return {"error": "No updates provided"}

        updates.append("updated_at = CURRENT_TIMESTAMP")

        conn = get_db_connection()
        cur = conn.cursor()
        query = f"UPDATE iot_products SET {', '.join(updates)} WHERE id = %s RETURNING id"
        params.append(product_id)
        cur.execute(query, tuple(params))
        row = cur.fetchone()
        if not row:
            return {"error": "Product not found"}
        conn.commit()
        cur.close()
        conn.close()
        return {"status": "success", "id": product_id}
    except Exception as e:
        return {"error": str(e)}

def delete_iot_product(product_id: int):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM iot_products WHERE id = %s RETURNING id", (product_id,))
        row = cur.fetchone()
        if not row:
            return {"error": "Product not found"}
        conn.commit()
        cur.close()
        conn.close()
        return {"status": "success", "id": product_id}
    except Exception as e:
        return {"error": str(e)}
