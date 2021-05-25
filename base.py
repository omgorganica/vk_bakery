import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
HOST = os.getenv("HOST")

engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{HOST}/{DB_NAME}')

Session = sessionmaker(bind=engine)

Base = declarative_base()