import os
import sys

sys.path.append(os.path.dirname(sys.path[0]))

from apscheduler.schedulers.blocking import BlockingScheduler

import service.schedule_weixin as service

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    # 添加定时任务，每天的 10 点和晚上 8 点执行
    scheduler.add_job(service.push_weather_to_weixin(), 'cron', hour='10,20')

    print('start success')
    # 启动调度器
    scheduler.start()
