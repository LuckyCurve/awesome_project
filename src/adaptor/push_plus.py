import requests
from enum import Enum
from utils import LOGGER

PUSH_PLUS_TOKEN = "aa7ea9fc16f546b6be55fa06965f8d33"


class MessageType(Enum):
    MARKDOWN = 'markdown'
    TXT = 'txt'


def send_message(message, title, template: MessageType):
    url = "http://www.pushplus.plus/send"
    params = {
        'token': PUSH_PLUS_TOKEN,
        'title': title,
        'content': message,
        'template': template.value,
    }
    LOGGER.info(fr'push plus request: {params}')
    response = requests.get(url, params=params)
    LOGGER.info(f"push plus response: {response.json()}")
