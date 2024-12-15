from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# הגדרת המודול של Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_management.settings')

app = Celery('inventory_management')

# טעינת הגדרות של Celery מתוך קובץ ההגדרות של Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# טעינת משימות מתוך אפליקציות Django
app.autodiscover_tasks()
