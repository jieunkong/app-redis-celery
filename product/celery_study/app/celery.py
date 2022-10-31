
from celery import Celery
from billiard import freeze_support
from celery import Celery, Task


class ConfigCelery:
    broker_url = "redis://redis:6379/0"
    result_backend = "redis://redis:6379/0"

    task_serializer = 'pickle'
    result_serializer = 'pickle'
    accept_content = ['json', 'pickle']
    timezone = 'Asia/Seoul'


celery = Celery('tasks')
celery.config_from_object(ConfigCelery)


if __name__ == '__main__':
    freeze_support()
    argv = [
        'worker',
        '--loglevel=WARNING',
        '--concurrency=1',
        '--pool=solo'
    ]
    celery.worker_main(argv)
