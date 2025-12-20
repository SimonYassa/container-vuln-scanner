from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base

class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    tag = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())

class Scan(Base):
    __tablename__ = "scans"
    id = Column(Integer, primary_key=True)
    image_id = Column(Integer, ForeignKey("images.id"), nullable=False)
    status = Column(String, default="pending")
    scan_time = Column(DateTime, server_default=func.now())

class Vulnerability(Base):
    __tablename__ = "vulnerabilities"
    id = Column(Integer, primary_key=True)
    scan_id = Column(Integer, ForeignKey("scans.id"), nullable=False)
    cve_id = Column(String, nullable=False)
    severity = Column(String)
    package = Column(String)
    description = Column(String)
