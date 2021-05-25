from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from db_commands import get_goods, get_categories


def category_keyboard():
    keyboard = VkKeyboard(inline=True)
    data = get_categories()

    for index, element in enumerate(data):
        keyboard.add_callback_button(element['name'],
                                     color=VkKeyboardColor.PRIMARY,
                                     payload={"type": "go_to_goods", "category_id": element['id']})

    return keyboard.get_keyboard()


def goods_keyboard(category_id):
    keyboard = VkKeyboard(inline=True)
    data = get_goods(category_id)

    for index,element in enumerate(data, start=0):
        payload = {"category": element['id']}
        keyboard.add_callback_button(element['name'], color=VkKeyboardColor.PRIMARY,
                                     payload={"type": "go_to_element", "element_id": element['id']})
        if index < len(data):
            keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)
    return keyboard.get_keyboard()





