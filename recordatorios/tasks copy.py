from huey import crontab
from huey.contrib.djhuey import periodic_task, task

@task()
def add_numbers(a, b):
    return a + b

@periodic_task(crontab(minute='*/5'))
def every_five_minutes():
    print("Esta tarea se ejecuta cada cinco minutos.")
