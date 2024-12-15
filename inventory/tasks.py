# # tasks.py
# from inventory_management.inventory_management.celery import Celery
# from inventory_management.inventory_management.celery import crontab
# from inventory_management.inventory_management.celery import shared_task
# from django.core.mail import send_mail
# from .models import Product
#
#
# @shared_task
# def send_daily_report():
#     products = Product.objects.all()
#     report = "Daily Report\n\n"
#     for product in products:
#         report += f"Product: {product.name}, Stock: {product.stock}\n"
#
#     send_mail(
#         'Daily Inventory Report',
#         report,
#         'from@example.com',
#         ['to@example.com'],
#         fail_silently=False,
#     )
#
#
# app = Celery('myproject')
#
# app.conf.beat_schedule = {
#     'send-daily-report': {
#         'task': 'myapp.tasks.send_daily_report',
#         'schedule': crontab(minute=0, hour=0),
#     },
# }
from inventory_management.celery import app
from celery.schedules import crontab
from celery import shared_task
from django.core.mail import send_mail
from .models import Product


@shared_task
def send_daily_report():
    products = Product.objects.all()
    report = "Daily Report\n\n"
    for product in products:
        report += f"Product: {product.name}, Stock: {product.stock}\n"

    send_mail(
        'Daily Inventory Report',
        report,
        'hinda40311@gmail.com',
        ['hinda40311@gmail.com'],
        fail_silently=False,
    )


app.conf.beat_schedule = {
    'send-daily-report': {
        'task': 'inventory_management.tasks.send_daily_report',
        'schedule': crontab(minute=0, hour=0),
    },
}
