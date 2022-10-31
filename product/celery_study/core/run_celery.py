import time
from billiard import freeze_support
from celery import Celery, Task


class ConfigCelery:
    broker_url = "redis://redis:6379/0"
    result_backend = "redis://redis:6379/0"

    task_serializer = 'pickle'
    result_serializer = 'pickle'
    accept_content = ['json', 'pickle']
    timezone = 'Asia/Seoul'


class UserTask(Task):

    def run(self, id):
        time.sleep(int(id) * 10)

        return f'core) worker response value: {id}'
        

app = Celery('tasks')
app.config_from_object(ConfigCelery)
app.register_task(UserTask())


if __name__ == '__main__':
    freeze_support()
    argv = [
        'worker',
        '--queues=core',
        '--loglevel=WARNING',
        '--concurrency=1',
        '--pool=solo'
    ]
    app.worker_main(argv)
    