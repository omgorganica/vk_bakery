from pprint import pprint
from typing import List

from base import Session
from models import Category, Good

session = Session()


def get_categories() -> List:
    categories = session.query(Category).all()
    cat_list = {cat.id:cat.name for cat in categories}
    return cat_list


def get_goods(category)-> List:
    goods_list = []
    goods = session.query(Good).join(Category).filter(Category.id == category)

    for good in goods:
        good_dict = {'id':good.id,'name':good.name,'description':good.description,'image':good.image }
        goods_list.append(good_dict)

    return goods_list

