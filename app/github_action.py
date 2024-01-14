import os
import sys

sys.path.append(os.path.dirname(sys.path[0]))

import service.schedule_weixin as service

if __name__ == '__main__':
    service.push_weather_to_weixin()
