from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


# Модель категорий товаров
class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    goods = relationship('Good', backref="goods")

    def __init__(self, name):
        self.name = name


# Модель товаров
class Good(Base):
    __tablename__ = 'goods'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    image = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    def __init__(self, name, description, image, category):
        self.name = name
        self.description = description
        self.image = image
        self.category_id = category
