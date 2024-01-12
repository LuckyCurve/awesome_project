from apscheduler.schedulers.blocking import BlockingScheduler
from src.service import weather
from src.service import push_plus


def get_weather_and_push_message():
    message = weather.get_weather()
    push_plus.text_message(message)


if __name__ == '__main__':
    get_weather_and_push_message()
    scheduler = BlockingScheduler()
    # 添加定时任务，每天的 10 点和晚上 8 点执行
    scheduler.add_job(get_weather_and_push_message, 'cron', hour='10,20')

    print('start success')
    # 启动调度器
    scheduler.start()
