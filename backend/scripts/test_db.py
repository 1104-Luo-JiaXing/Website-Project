import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

url = os.getenv("DATABASE_URL")
print("Connecting...")

engine = create_engine(url)
with engine.connect() as conn:
    version = conn.execute(text("select version()")).scalar()
    print("Connected.")
    print(version)