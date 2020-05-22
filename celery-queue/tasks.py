import os
import time
from celery import Celery


CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

SMS_USE = True

SMS_HOST = "172.17.0.1"
SMS_PORT = "10200"

SMS_USERNAME = "pfsmser"
SMS_PASSWORD = "pfsmser666"
SMS_MSG_TEMPLATE = "Witaj%20w%20Plus%20Fun!%20Twoj%20kod%20SMS:%20{}"

SMS_PATH = "http://{}:{}/cgi-bin/sendsms?user={}&pass={}&text={}&to={}&from=PlusFun"

@celery.task(name='tasks.add')
def add(x: int, y: int) -> int:
    time.sleep(5)
    print(''+str(x)+'-'+str(y))
    return x + y
    
# @celery.task(name='tasks.sendSMS')
# def sendSMS(to: str, msg: str) ->str:
#     print('send message '+msg)
#     # import requests
#     # request_url = SMS_PATH.format(SMS_HOST, SMS_PORT, SMS_USERNAME, SMS_PASSWORD, SMS_MSG_TEMPLATE.format(msg), to)
#     # res = requests.get(request_url)
#     # print(res)
#     # return res.text
#     return msg

@celery.task(name='tasks.sendSMS')
def sendSMS(to: str, msg: str) ->str:
    print('send message '+msg)
    # logger.info('send message '+msg)
    import requests
    request_url = SMS_PATH.format(SMS_HOST, SMS_PORT, SMS_USERNAME, SMS_PASSWORD, SMS_MSG_TEMPLATE.format(msg), to)
    res = requests.get(request_url)
    # print(res)
    # logger.info(res)
    return res.text