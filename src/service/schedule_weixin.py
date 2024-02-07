from adaptor import push_plus, weather


def push_weather_to_weixin():
    message = weather.get_weather()
    push_plus.send_message(message, '天气预警', push_plus.MessageType.MARKDOWN)


def test_push_weather_to_weixin():
    push_weather_to_weixin()
