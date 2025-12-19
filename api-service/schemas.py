from pydantic import BaseModel

class ScanRequest(BaseModel):
    image_name: str

class ScanResponse(BaseModel):
    scan_id: int
    status: str
