from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from db_commands import get_goods, get_categories


# Клавиатура для начала диалога
def category_keyboard():
    keyboard = VkKeyboard(inline=True)
    data = get_categories()
    for element in data:
        keyboard.add_callback_button(element['name'],
                                     color=VkKeyboardColor.PRIMARY,
                                     payload={"type": "go_to_goods", "category_id": element['id']})

    return keyboard.get_keyboard()


# Клавиатура с доступными категориями товаров
def goods_keyboard(category_id):
    keyboard = VkKeyboard(inline=True)
    data = get_goods(category_id)
    for index, element in enumerate(data, start=0):
        keyboard.add_callback_button(element['name'], color=VkKeyboardColor.PRIMARY,
                                     payload={"type": "go_to_element", "element_id": element['id']})
        if index < len(data): # Делаем по 1 кнопке в ряду
            keyboard.add_line()
    keyboard.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE, payload={"type": "go_to_categories"})
    return keyboard.get_keyboard()


# Клавиатура с доступными товарами внутри выбранной категории
def element_keyboard(category_id):
    keyboard = VkKeyboard(inline=True)
    keyboard.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE,
                                 payload={"type": "go_to_goods", "category_id": category_id, "back": True})
    return keyboard.get_keyboard()
