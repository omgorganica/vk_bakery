import os
import vk_api.vk_api
from random import random
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from vk_api.upload import VkUpload
from keyboards import category_keyboard, goods_keyboard, element_keyboard
from db_commands import get_element
from dotenv import load_dotenv
load_dotenv()


class Server:
    def __init__(self, api_token, group_id, server_name: str = "New server"):
        # Имя нашего сервера
        self.server_name = server_name
        # Для Long Poll
        self.vk = vk_api.VkApi(token=api_token)
        # Для использования Long Poll API
        self.long_poll = VkBotLongPoll(self.vk, group_id)
        # Для вызова методов vk_api
        self.vk_api = self.vk.get_api()

    # Отправка сообщения через метод messages.send
    def send_msg(self, send_id, message):
        self.vk_api.messages.send(peer_id=send_id, message=message, random_id=random())

    # Посылаем тестовое сообщение пользователю с указанным ID
    def test(self):
        vk_user = os.getenv("VK_USER")
        self.send_msg(vk_user, f"Если ты это читаешь, значит бот {self.server_name} запущен")

    # Получаем имя пользователя
    def get_user_name(self, user_id):
        return self.vk_api.users.get(user_id=user_id)[0]['first_name']

    # Функция отправки сообщения пользователю
    def send_message(self, peer_id, message, keyboard=None, attachment=None):
        self.vk_api.messages.send(peer_id=peer_id, message=message, random_id=random(), keyboard=keyboard,
                                  attachment=attachment)

    # Сообщение, реагирующее на начало диалога
    def send_initial_message(self, event):
        username = self.get_user_name(event.object.from_id)
        self.send_message(event.object.peer_id,
                          f"Приветствую,{username}.Вкусняшек какого стиля тебе хочется?",
                          keyboard=category_keyboard())

    # Сообщение,реагириющее на выбор категории
    def send_category_message(self, event):
        category_id = event.object.payload.get('category_id')
        self.send_message(event.object.peer_id,
                          "У нас есть много всего,выбирай",
                          keyboard=goods_keyboard(category_id))

    # Сообщение, реагирующее на выбор товара
    def send_element_message(self, event):
        element_id = event.object.payload.get('element_id')
        element = get_element(element_id)
        category_id = element['category']
        upload = VkUpload(self.vk)
        upload_photo_response = upload.photo_messages(photos=element['image'])[0]
        photo = f"photo{upload_photo_response['owner_id']}_{upload_photo_response['id']}"
        text = f"Вкусняшка:{element['name']} \n" \
               f"Описание:{element['description']}"
        self.send_message(event.object.peer_id,
                          text,
                          keyboard=element_keyboard(category_id),
                          attachment=photo)

    # Сообщение возврата к списку категорий
    def send_back_to_category_message(self, event):
        category_id = event.object.payload.get('category_id')
        self.send_message(event.object.peer_id,
                          "У нас есть много всего,выбирай",
                          keyboard=goods_keyboard(category_id))

    # Сообщение возврата к начальному экрану
    def send_to_initial_message(self, event):
        self.send_message(event.object.peer_id,
                          "Вкусняшек какого стиля тебе хочется?",
                          keyboard=category_keyboard())

    # Основная функция работы бота
    def start(self):
        for event in self.long_poll.listen():
            # Реакция на сообщения без callback data
            if event.type == VkBotEventType.MESSAGE_NEW:
                self.send_initial_message(event)

            # Реакция на сообщения с callback data из кнопок
            if event.type == VkBotEventType.MESSAGE_EVENT:
                if event.object.payload.get('type') == 'go_to_goods':
                    self.send_category_message(event)

                if event.object.payload.get('type') == 'go_to_element':
                    self.send_element_message(event)

                if event.object.payload.get('type') == 'go_to_goods' and event.object.payload.get('back') == True:
                    self.send_back_to_category_message(event)

                if event.object.payload.get('type') == 'go_to_categories':
                    self.send_to_initial_message(event)
