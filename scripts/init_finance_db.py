import os
import psycopg2
from app.core.database import get_db_connection

def init_finance_db():
    """Cria as tabelas necessárias para o módulo de finanças."""
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        # Tabela de Contas
        cur.execute("""
            CREATE TABLE IF NOT EXISTS finance_accounts (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                name VARCHAR(255) NOT NULL,
                account_type VARCHAR(50) NOT NULL,
                balance DECIMAL(15, 2) DEFAULT 0.0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        # Tabela de Categorias
        cur.execute("""
            CREATE TABLE IF NOT EXISTS finance_categories (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                name VARCHAR(100) NOT NULL,
                parent_id INTEGER REFERENCES finance_categories(id),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        # Tabela de Grupos de Parcelamento
        cur.execute("""
            CREATE TABLE IF NOT EXISTS finance_installment_groups (
                id SERIAL PRIMARY KEY,
                total_amount DECIMAL(15, 2) NOT NULL,
                total_installments INTEGER NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        # Tabela de Transações
        cur.execute("""
            CREATE TABLE IF NOT EXISTS finance_transactions (
                id SERIAL PRIMARY KEY,
                account_id INTEGER NOT NULL REFERENCES finance_accounts(id),
                category_id INTEGER NOT NULL REFERENCES finance_categories(id),
                date TIMESTAMP NOT NULL,
                amount DECIMAL(15, 2) NOT NULL,
                description TEXT NOT NULL,
                transaction_type VARCHAR(20) NOT NULL,
                is_recurring BOOLEAN DEFAULT FALSE,
                installment_group_id INTEGER REFERENCES finance_installment_groups(id),
                installment_number INTEGER,
                source_metadata JSONB DEFAULT '{}',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        conn.commit()
        print("Tabelas de finanças criadas com sucesso!")
        
    except Exception as e:
        conn.rollback()
        print(f"Erro ao inicializar banco de dados de finanças: {e}")
        raise e
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    init_finance_db()
