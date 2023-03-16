from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Response
from django.conf import settings


def notify_authors_response(pk, text, author):
    html_content = render_to_string(
        'response_created.html',
        {
            'text': text,
            'link': f'{settings.SITE_URL}/ads/response/{pk}'
        }
    )
    msg = EmailMultiAlternatives(
        subject=f'{Response.ad}',
        body=f'{Response.text}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=author
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_notifications(preview, pk, title, user):
    html_contest = render_to_string(
        'ad_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/ads/{pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=user,
    )

    msg.attach_alternative(html_contest, 'text/html')
    msg.send()
