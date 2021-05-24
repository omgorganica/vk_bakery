import os
from dotenv import load_dotenv
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

load_dotenv()


def main() -> None:
    token = os.getenv("TOKEN")
    vk_session = vk_api.VkApi(token=token)
    long_poll = VkBotLongPoll(vk_session, 204765770)
    vk = vk_session.get_api()

    for event in long_poll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            peer_id = event.obj['peer_id']
            message = event.obj['text'].lower()

            if message == 'привет':
                vk.messages.send(
                    peer_id=peer_id,
                    message='Привет!',
                    random_id=get_random_id(),
                )


if __name__ == '__main__':
    main()


