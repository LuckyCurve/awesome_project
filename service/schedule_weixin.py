import adaptor.weather as weather
import adaptor.push_plus as push_plus


def push_weather_to_weixin():
    message = weather.get_weather()
    push_plus.text_message(message)
