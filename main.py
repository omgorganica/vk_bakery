from db_commands import get_goods, get_categories
import vk_api.vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType

data = get_categories()
for el in data:
    print(el['id'])