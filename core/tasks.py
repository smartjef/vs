from celery import shared_task
from django.core.mail import send_mail
from .models import Contact

@shared_task
def send_email(contact_id):
    """
    Task to send an e-mail notification when an contact for is filled
    successfully.
    """
    contact = Contact.objects.get(id=contact_id)
    subject = f'Contact | { contact.subject }'
    message = f'Dear Support, { contact.name } filled contact form,\n\n' \
    f'{ contact.message }.'\
    f'Email - { contact.email }'
    mail_sent = send_mail(subject, message, 'no-reply@vstech.co.ke', ['o.jeff3.a@gmail.com'])

    return mail_sent