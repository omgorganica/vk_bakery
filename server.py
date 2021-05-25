import vk_api.vk_api
from random import random
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from keyboards import category_keyboard, goods_keyboard, back_keyboard
from db_commands import get_element


class Server:

    def __init__(self, api_token, group_id, server_name: str = "New server"):
        # Даем серверу имя
        self.server_name = server_name

        # Для Long Poll
        self.vk = vk_api.VkApi(token=api_token)

        # Для использования Long Poll API
        self.long_poll = VkBotLongPoll(self.vk, group_id)

        # Для вызова методов vk_api
        self.vk_api = self.vk.get_api()

    def send_msg(self, send_id, message):
        """
        Отправка сообщения через метод messages.send
        :param send_id: vk id пользователя, который получит сообщение
        :param message: содержимое отправляемого письма
        :return: None
        """
        self.vk_api.messages.send(peer_id=send_id,
                                  message=message,
                                  random_id=random())

    def test(self):
        # Посылаем сообщение пользователю с указанным ID
        self.send_msg(50113631, "Привет-привет!")

    def get_user_name(self, user_id):
        """ Получаем имя пользователя"""
        return self.vk_api.users.get(user_id=user_id)[0]['first_name']

    def get_user_city(self, user_id):
        """ Получаем город пользователя"""
        return self.vk_api.users.get(user_id=user_id, fields="city")[0]["city"]['title']

    def send_message(self, peer_id, message, keyboard=None):
        self.vk_api.messages.send(peer_id=peer_id, message=message, random_id=random(), keyboard=keyboard)

    def start(self):
        for event in self.long_poll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                username = self.get_user_name(event.object.from_id)
                print(event)

                self.send_message(event.object.peer_id,
                                  f"Приветствую,{username}.Вкусняшек какого стиля тебе хочется?",
                                  keyboard=category_keyboard())

            if event.type == VkBotEventType.MESSAGE_EVENT:
                print(event)
                if event.object.payload.get('type') == 'go_to_goods':
                    category_id = event.object.payload.get('category_id')
                    self.send_message(event.object.peer_id,
                                      "У нас есть много всего,выбирай",
                                      keyboard=goods_keyboard(category_id))

                if event.object.payload.get('type') == 'go_to_element':
                    element_id = event.object.payload.get('element_id')
                    element = get_element(element_id)
                    text = f"Вкусняшка:{element['name']} \n" \
                           f"Описание:{element['description']}"
                    self.send_message(event.object.peer_id,
                                      text,
                                      keyboard=back_keyboard())
