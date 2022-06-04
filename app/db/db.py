import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


def get_db_settings():
    """Get database environment variables.

    Returns:
        _dict_: Environment variables related to DB connection.
    """
    return {
        "DB_USERNAME": os.getenv('DB_USERNAME'),
        "DB_PASSWORD": os.getenv('DB_PASSWORD'),
        "DB_HOST": os.getenv('DB_HOST'),
        "DB_PORT": os.getenv('DB_PORT'),
        "DB_NAME": os.getenv('DB_NAME'),
    }


settings = get_db_settings()
print(settings)
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.get('DB_USERNAME')}:{settings.get('DB_PASSWORD')}@{settings.get('DB_HOST')}:{settings.get('DB_PORT')}/{settings.get('DB_NAME')}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """Get database session.

    Yields:
        _sessionmaker_: The database session. 
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
