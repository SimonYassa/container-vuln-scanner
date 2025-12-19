from database import engine

try:
    engine.connect()
    print("Connected to PostgreSQL ✅")
except Exception as e:
    print("Failed ❌", e)
