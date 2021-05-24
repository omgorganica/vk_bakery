import os
import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, MetaData, String, ForeignKey
from dotenv import load_dotenv

# Создания движка базы данных
load_dotenv()  # загрузка .env файла
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
HOST = os.getenv("HOST")
engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{HOST}/{DB_NAME}')


def connect(user, password, db):
    url = f'postgresql+psycopg2://{user}:{password}@localhost/{db}'
    con = sqlalchemy.create_engine(url, client_encoding='utf8')
    meta = sqlalchemy.MetaData(bind=con)

    return con, meta


con, meta = connect(DB_USER, DB_PASSWORD, DB_NAME)

categories = Table('categories', meta,
                   Column('id', Integer, primary_key=True),
                   Column('name', String))

goods = Table('goods', meta,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('description', String),
              Column('category', ForeignKey('categories.id', ondelete='CASCADE'), nullable=False),
              Column('image', String))

meta.create_all(con)

categories = [
    {'name': 'Black'},
    {'name': 'Trash'},
    {'name': 'Classic'},
]
goods = [
    {'name': 'Buzrum pancakes', 'description': 'Lorem ipsum dolor', "category": '1', "image": "..Images/cake.jpg"},
    {'name': 'Dimmu Borgir sweets', 'description': 'Lorem ipsum dolor', "category": '1', "image": "..Images/cake.jpg"},
    {'name': 'Behemoth jelly', 'description': 'Lorem ipsum dolor', "category": '1', "image": "..Images/cake.jpg"},
    {'name': 'Metallica pods', 'description': 'Lorem ipsum dolor', "category": '2', "image": "..Images/cake.jpg"},
    {'name': 'Slayer honey', 'description': 'Lorem ipsum dolor', "category": '2', "image": "..Images/cake.jpg"},
    {'name': 'Pantera marshmallow', 'description': 'Lorem ipsum dolor', "category": '2', "image": "..Images/cake.jpg"},
    {'name': 'Ozzy sweet powder', 'description': 'Lorem ipsum dolor', "category": '3', "image": "..Images/cake.jpg"},
    {'name': 'Iron Maiden donuts', 'description': 'Lorem ipsum dolor', "category": '3', "image": "..Images/cake.jpg"},
    {'name': 'Judas Priest pie', 'description': 'Lorem ipsum dolor', "category": '3', "image": "..Images/cake.jpg"},
]
#Создать записи в БД
# con.execute(meta.tables['categories'].insert(), categories)
# con.execute(meta.tables['goods'].insert(), goods)

