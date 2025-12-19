from sqlalchemy.orm import Session
import models

def get_or_create_image(db: Session, image_name: str):
    image = db.query(models.Image).filter_by(name=image_name).first()
    if not image:
        image = models.Image(name=image_name)
        db.add(image)
        db.commit()
        db.refresh(image)
    return image

def create_scan(db: Session, image_id: int):
    scan = models.Scan(image_id=image_id, status="pending")
    db.add(scan)
    db.commit()
    db.refresh(scan)
    return scan
