from pydantic import BaseModel
from typing import List, Optional

class ImageRequest(BaseModel):
    name: str
    tag: Optional[str] = None

class ScanRequest(BaseModel):
    image_name: str

class VulnerabilityResponse(BaseModel):
    cve_id: str
    severity: str
    package: str
    description: str

class ScanDetailResponse(BaseModel):
    scan_id: int
    status: str
    image_name: str
    scan_date: str
    vulnerabilities: List[VulnerabilityResponse]

class ScanResponse(BaseModel):
    scan_id: int
    status: str
    image_name: str
