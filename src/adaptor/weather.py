import json

import requests
from ..utils import LOGGER


def get_weather():
    url = 'https://restapi.amap.com/v3/weather/weatherInfo'
    params = {
        'key': '8b8d67507c4977e68eb26bdf2881bc5f',
        'city': '440305',
        'extensions': 'all'
    }

    res = ''
    SPLIT = '\n\n'

    LOGGER.info(fr'get weather request params: {params}')

    response = requests.get(url, params=params).json()
    base_info = next(iter(response['forecasts']))

    res += format(f'### {base_info["province"]}省{base_info["city"]}' + SPLIT)
    for cast in base_info['casts']:
        res += f'{cast["date"]}\t白天天气：{cast["dayweather"]}\t夜间天气：{cast["nightweather"]}' + SPLIT

    LOGGER.info(f'get weather response: {json.dumps(response, ensure_ascii=False)}')

    return res