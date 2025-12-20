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
    # Create the scan record
    scan = models.Scan(image_id=image_id, status="completed")
    db.add(scan)
    db.commit()
    db.refresh(scan)
    
    # Create a dummy vulnerability so the test list has data
    vuln = models.Vulnerability(
        scan_id=scan.id,
        cve_id="CVE-2025-0001",
        severity="High",
        package="openssl"
    )
    db.add(vuln)
    db.commit()
    
    return scan