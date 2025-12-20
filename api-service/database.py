import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# RULE COMPLIANCE:
# 1. Check if the full DATABASE_URL environment variable exists (from Kubernetes)
# 2. If not, fall back to building it manually (for local Docker testing)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    # We are likely running locally in Docker, not K8s yet
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    db_name = os.getenv("POSTGRES_DB", "vulnscanner")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5433")
    
    DATABASE_URL = f"postgresql://{user}:{password}@{db_host}:{db_port}/{db_name}"

print(f"--> USING DATABASE URL: {DATABASE_URL}")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()