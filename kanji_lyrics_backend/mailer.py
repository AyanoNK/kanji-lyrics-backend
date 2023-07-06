from django.template import Context
from django.core.mail import EmailMessage
from django.conf import settings


def send_review_email(email, subject, content):
    email = EmailMessage(
        subject, content,
        settings.DEFAULT_FROM_EMAIL, [email],
    )

    return email.send(fail_silently=False)
