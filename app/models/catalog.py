from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class IoTDeviceBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    brand: Optional[str] = Field(None, max_length=100)
    protocol: Optional[str] = Field(None, max_length=50)
    payload_yaml: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

class IoTDeviceCreate(IoTDeviceBase):
    pass

class IoTDeviceUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    brand: Optional[str] = Field(None, max_length=100)
    protocol: Optional[str] = Field(None, max_length=50)
    payload_yaml: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

class IoTDevice(IoTDeviceBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class RAGQuery(BaseModel):
    query: str
    top_k: Optional[int] = 5

class RAGResult(BaseModel):
    content: str
    metadata: Dict[str, Any]
    source: Optional[str]
    score: float
