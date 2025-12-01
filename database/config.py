from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase

DATABASE_URL="sqlite:///./job_portal_system.db"

engine=create_engine(DATABASE_URL)

Session=sessionmaker(bind=engine,autoflush=False)

class Base(DeclarativeBase):
    pass