from pprint import pprint
from typing import List, Dict

from base import Session
from models import Category, Good

session = Session()


def get_categories() -> List:
    cat_list = []
    categories = session.query(Category).all()
    for cat in categories:
        new_item = {"id": cat.id, "name": cat.name}
        cat_list.append(new_item)
    return cat_list


def get_goods(category_id) -> List:
    goods_list = []
    goods = session.query(Good).join(Category).filter(Category.id == category_id)

    for good in goods:
        good_dict = {'id': good.id, 'name': good.name}
        goods_list.append(good_dict)

    return goods_list


def get_element(element_id) -> Dict:
    element = {}
    goods = session.query(Good).filter(Good.id == element_id).first()
    element['name'] = goods.name
    element['description'] = goods.description
    element['image'] = goods.image
    element['category'] = goods.category_id

    return element

