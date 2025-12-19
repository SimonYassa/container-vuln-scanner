from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base

class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    created_at = Column(DateTime, server_default=func.now())

class Scan(Base):
    __tablename__ = "scans"
    id = Column(Integer, primary_key=True)
    image_id = Column(Integer, ForeignKey("images.id"))
    status = Column(String)
    created_at = Column(DateTime, server_default=func.now())

class Vulnerability(Base):
    __tablename__ = "vulnerabilities"
    id = Column(Integer, primary_key=True)
    scan_id = Column(Integer, ForeignKey("scans.id"))
    cve_id = Column(String)
    severity = Column(String)
    package = Column(String)
