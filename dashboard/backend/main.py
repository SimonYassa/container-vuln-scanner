from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development, allows any origin
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.get("/scans")
def get_scans():
    return [
        {
            "image_name": "nginx:latest",
            "scan_date": "2025-12-19",
            "vulnerabilities": [
                {"cve": "CVE-2025-1234", "severity": "HIGH"},
                {"cve": "CVE-2025-5678", "severity": "LOW"}
            ]
        },
        {
            "image_name": "redis:6.2",
            "scan_date": "2025-12-18",
            "vulnerabilities": [
                {"cve": "CVE-2025-9999", "severity": "CRITICAL"}
            ]
        }
    ]
