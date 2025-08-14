# =====================================================
# Database connection setup using SQLAlchemy for PostgreSQL
# =====================================================
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# TODO: Replace with Render PostgreSQL credentials
DB_USER = 'pavan'
DB_PASSWORD = 'rPDB4gfiyUZQGBlsF4OG5NjKHIGq0fRp'
DB_HOST = 'dpg-d2ep8o6r433s738ch5v0-a'   # e.g., your-db-name.render.com
DB_NAME = 'lms_db_lpkg'

# SQLAlchemy connection string for PostgreSQL
DATABASE_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

# Create engine and session
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
