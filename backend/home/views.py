from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import socket


def home(request):
    return render(request, 'home/home.html', {
        'is_prod': settings.PROD,
        'is_prerelease': settings.PRERELEASE,
        'hostname': socket.gethostname()
    })