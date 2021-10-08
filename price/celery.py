import os
from celery.schedules import crontab

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AlphaVantage.settings')

app = Celery('price')
app.config_from_object('django.conf:settings')

app.conf.beat_schedule = {
    'add-price_task-every-1-hour': {
        'task': 'price.tasks.periodic_task_fetch_price',
        'schedule': crontab(minute='*/1')
    },
}
# app.conf.timezone = 'UTC'

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
