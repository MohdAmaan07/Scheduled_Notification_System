import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Scheduled_Notification_System.settings')

app = Celery('backend')
app.config_from_object('django.conf.settings', namespace='CELERY')

app.conf.beat_schedule = {
    'send-daily-reports': {
        'task': 'notifications.tasks.send_daily_updates',
        'schedule': crontab(hour=8, minute=0),  
        'args': (),
    },
}

app.autodiscover_tasks()
