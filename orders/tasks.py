from celery import shared_task
from django.core.mail import send_mail

from .models import Order

@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order #{order.id}'
    message = f'Dear {order.first_name}!\n\n' \
            f'You have succefully placed an order' \
            f'Your order id is {order.id}.'
    mail_send = send_mail(subject, message, 'dimaluz@rambler.ru', [order.email])
    return mail_send
    