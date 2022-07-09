from django.http import HttpResponse
from django.shortcuts import render

from app.tasks import mailer, uploader

def mail_queue_view(request):
    mailer.delay()
    return HttpResponse("[MAIL QUEUE] Sending emails")

def upload_queue_view(request):
    uploader.delay()
    return HttpResponse("[UPLOAD QUEUE] Uploading files")
