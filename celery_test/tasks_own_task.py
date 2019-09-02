from celery import Celery
from celery import Task

class MyTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print("on success")
    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        print("after return")
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print("on failure")

app = Celery('tasks',
        broker='redis://127.0.0.1:6379',
        backend='redis://127.0.0.1:6379'
             )



@app.task(base=MyTask)
def add(x, y):
    return x + y

@app.task(base=MyTask)
def error(x, y):
    return 1/0
