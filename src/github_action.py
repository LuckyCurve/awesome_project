import service.schedule_weixin as service
from utils import LOGGER

if __name__ == '__main__':
    LOGGER.info("execute github action")
    service.push_weather_to_weixin()
