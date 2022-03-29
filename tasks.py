#!/usr/bin/env python3
from celery import Celery
from oom import oom


app = Celery('tasks', broker='redis://redis-master')


oom = app.task(oom)
oom.delay()
