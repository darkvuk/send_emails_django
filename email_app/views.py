from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    title = 'Naslov'
    receivers = ['darko.vukasovic5@gmail.com']
    message = '<h1 color="red">Tekst mejla</h1>'

    send_mail(
        subject=title,
        message='',
        html_message=message,
        from_email='settings.EMAIL_HOST_USER',
        recipient_list=receivers,
        fail_silently=False
    )

    return HttpResponse('Done.')
