import os
from server import Server
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
COMMUNITY = os.getenv("COMMUNITY_ID")

server1 = Server(TOKEN, COMMUNITY, "Metall-Bakery")  # Создание нового сервера
server1.test()  # Проверка работы бота
server1.start()  # Запуск бота
