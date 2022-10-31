# import time
# from celery import Task


# class UserTask(Task):

#     def run(self, id):
#         time.sleep(int(id) * 10)

#         return f'core) worker response value: {id}'