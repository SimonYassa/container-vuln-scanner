from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Container Vulnerability Scanner API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/scan", response_model=schemas.ScanResponse)
def scan_image(req: schemas.ScanRequest, db: Session = Depends(get_db)):
    image = crud.get_or_create_image(db, req.image_name)
    scan = crud.create_scan(db, image.id)
    return {"scan_id": scan.id, "status": scan.status}

@app.get("/scans")
def get_scans(db: Session = Depends(get_db)):
    scans = db.query(models.Scan).all()
    return scans
