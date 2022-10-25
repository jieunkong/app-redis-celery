import time
from celery import Celery

celery = Celery(__name__)
celery.conf.broker_url = "redis://redis:6379/0"
celery.conf.result_backend = "redis://redis:6379/0"


@celery.task(name="create_task")
def create_task(id):
    time.sleep(int(id) * 10)
    
    return f'worker response value: {id}'