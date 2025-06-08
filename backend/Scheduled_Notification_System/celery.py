from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Scheduled_Notification_System.settings')

app = Celery('Scheduled_Notification_System')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-daily-reports': {
        'task': 'notifications.tasks.send_daily_updates',
        'schedule': crontab(hour=0, minute=0),  
    },
}
