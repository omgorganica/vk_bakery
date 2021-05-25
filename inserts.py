from base import Session, engine, Base
from models import Category, Good
from initial_data import goods_list, categories_list

# Создаем таблицы
Base.metadata.create_all(engine)
session = Session()

# Заполняем таблицы начальными данными
for category in categories_list:
    new_cat = Category(**category)
    session.add(new_cat)
for good in goods_list:
    new_good = Good(**good)
    session.add(new_good)

# Сохраняем измененя, закрываем сессию с БД
session.commit()
session.close()
