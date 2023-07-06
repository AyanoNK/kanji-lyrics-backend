from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_review_email(name: str, email: str, subject: str, content_template: str):
    context = {
        'name': name,
        'email': email,
    }

    email_body = render_to_string(content_template, context)

    email = EmailMessage(
        subject, email_body,
        settings.DEFAULT_FROM_EMAIL, [email],
    )

    return email.send(fail_silently=False)
