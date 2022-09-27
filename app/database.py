from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
from dotenv import load_dotenv

load_dotenv()
##postgresql+psycopg2://user:password@host:port/dbname
##'postgresql://postgres:password@localhost:5432/scooter'
#SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost:5432/scooter" 
SQLALCHEMY_DATABASE_URI = os.getenv("FLASK_POSTGRES_TARGET_DATABASE_URI")
engine = create_engine(url= SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    ##import app.models
    Base.metadata.create_all(bind=engine)