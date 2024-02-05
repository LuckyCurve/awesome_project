import requests

PUSH_PLUS_TOKEN = "aa7ea9fc16f546b6be55fa06965f8d33"

def text_message(message, title, template):
    url = "http://www.pushplus.plus/send"
    params = {
        'token': PUSH_PLUS_TOKEN,
        'title': title,
        'content': message,
        'template': template,
    }
    response = requests.get(url, params=params)
    print(f"push plus response: {response.json()}")


if __name__ == '__main__':
    text_message("测试消息体", '天气预警', 'txt')
