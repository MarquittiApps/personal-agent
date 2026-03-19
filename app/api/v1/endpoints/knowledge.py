import os
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException, Body
from typing import List, Optional, Dict, Any
from app.models.catalog import IoTDevice, IoTDeviceCreate, IoTDeviceUpdate, RAGQuery, RAGResult
from app.core.rag_engine import (
    update_knowledge_base,
    query_knowledge_base,
    add_iot_product,
    get_iot_products,
    update_iot_product,
    delete_iot_product
)

router = APIRouter(prefix="/knowledge", tags=["knowledge"])

@router.post("/upload", status_code=201)
async def upload_pdf(file: UploadFile = File(...), metadata_json: Optional[str] = Body(None)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    # Save file temporarily
    temp_dir = "temp_uploads"
    os.makedirs(temp_dir, exist_ok=True)
    file_path = os.path.join(temp_dir, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        import json
        metadata = json.loads(metadata_json) if metadata_json else {}
        result = update_knowledge_base(file_path, metadata)

        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])

        return result
    finally:
        # Cleanup
        if os.path.exists(file_path):
            os.remove(file_path)

@router.post("/query", response_model=List[RAGResult])
async def query_rag(query_data: RAGQuery):
    results = query_knowledge_base(query_data.query, query_data.top_k)
    if isinstance(results, dict) and "error" in results:
        raise HTTPException(status_code=500, detail=results["error"])
    return results

# IoT Catalog Endpoints
@router.post("/catalog", response_model=IoTDevice, status_code=201)
async def create_device(device: IoTDeviceCreate):
    result = add_iot_product(
        name=device.name,
        brand=device.brand,
        protocol=device.protocol,
        payload_yaml=device.payload_yaml,
        metadata=device.metadata
    )
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.get("/catalog", response_model=List[IoTDevice])
async def list_devices():
    results = get_iot_products()
    if isinstance(results, dict) and "error" in results:
        raise HTTPException(status_code=500, detail=results["error"])
    return results

@router.patch("/catalog/{device_id}", response_model=Dict[str, Any])
async def patch_device(device_id: int, device: IoTDeviceUpdate):
    result = update_iot_product(
        product_id=device_id,
        name=device.name,
        brand=device.brand,
        protocol=device.protocol,
        payload_yaml=device.payload_yaml,
        metadata=device.metadata
    )
    if "error" in result:
        status_code = 404 if "not found" in result["error"].lower() else 400
        raise HTTPException(status_code=status_code, detail=result["error"])
    return result

@router.delete("/catalog/{device_id}", response_model=Dict[str, Any])
async def remove_device(device_id: int):
    result = delete_iot_product(device_id)
    if "error" in result:
        status_code = 404 if "not found" in result["error"].lower() else 400
        raise HTTPException(status_code=status_code, detail=result["error"])
    return result
