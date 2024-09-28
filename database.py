from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import loadenv
import os 

#loading the env file 
loadenv()

#DATABASE URL
DATABASE_URL = os.getenv("DATABASEURL")

Base = declarative_base


# implementing the sessionmaker
SessionLocal = sessionmaker(autocommit = False , autoFlush =False ,bind =engine )

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()