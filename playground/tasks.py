from time import sleep
from celery import shared_task

#if use decorator - @celery.task (this app(playground) is no longer independent and reusable, always need storefront folder )
@shared_task
def notify_customers(message):
    print('Sending 10k emails..')
    print(message)
    sleep(10)
    print('Emails were succcessfuly sent!')