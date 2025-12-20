from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud

# Initialize database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Container Vulnerability Scanner API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Container Vulnerability Scanner API"}

@app.get("/health")
def health_check():
    return {"status": "API is running"}

@app.post("/scan", response_model=schemas.ScanResponse)
def scan_image(req: schemas.ScanRequest, db: Session = Depends(get_db)):
    image = crud.get_or_create_image(db, req.image_name)
    scan = crud.create_scan(db, image.id)
    return {"scan_id": scan.id, "status": scan.status}

@app.get("/scans")
def get_scans(db: Session = Depends(get_db)):
    return db.query(models.Scan).all()

@app.get("/scans/{scan_id}")
def get_scan_details(scan_id: int, db: Session = Depends(get_db)):
    scan = db.query(models.Scan).filter(models.Scan.id == scan_id).first()
    if not scan:
        raise HTTPException(status_code=404, detail="Scan not found")
    return scan

@app.get("/vulnerabilities/{scan_id}")
def get_vulnerabilities(scan_id: int, db: Session = Depends(get_db)):
    return db.query(models.Vulnerability).filter(models.Vulnerability.scan_id == scan_id).all()