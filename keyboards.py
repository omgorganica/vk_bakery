from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from db_commands import get_goods, get_categories


def initial_keyboard():
    keyboard = VkKeyboard()
    data = get_categories()

    for element in data:
        payload = {"category": element['id']}
        keyboard.add_button(element['name'], color=VkKeyboardColor.PRIMARY, payload=payload)
    return keyboard.get_keyboard()
