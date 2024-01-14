from adaptor import push_plus, weather


def push_weather_to_weixin():
    message = weather.get_weather()
    push_plus.text_message(message)
