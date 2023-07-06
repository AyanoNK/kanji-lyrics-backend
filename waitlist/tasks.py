from celery.decorators import task
from celery.utils.log import get_task_logger
from kanji_lyrics_backend.mailer import send_success_waitlist_email
from django.template.loader import render_to_string


logger = get_task_logger(__name__)


@task(name="send_success_waitlist_email_task")
def send_success_waitlist_email_task(email: str):
    context = {
        'email': email,
    }
    subject = "Kanji Lyrics - Waitlist Success"
    email_body = render_to_string('waitlist.html', context)
    logger.info("Sending waitlist success email")
    return send_success_waitlist_email(email, subject, email_body)
