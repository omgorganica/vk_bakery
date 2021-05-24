import os
from server import Server
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
COMMUNITY = os.getenv("COMMUNITY_ID")

server1 = Server(TOKEN, COMMUNITY, "Metall-Bakery")
# vk_api_token - API токен, который мы ранее создали
# 172998024 - id сообщества-бота
# "server1" - имя сервера

server1.test()