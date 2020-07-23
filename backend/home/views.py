from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import socket


def home(request):

    with open(settings.TESTING_SECRET) as contents:
        extra = contents.read()

    return render(
        request,
        "home/home.html",
        {
            "is_prod": settings.PROD,
            "is_prerelease": settings.PRERELEASE,
            "hostname": socket.gethostname(),
            "consul_host": settings.CONSUL_ADDR,
            "extra": extra,
        },
    )

