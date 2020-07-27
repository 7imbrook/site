from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from utils.react import render_entrypoint


def home(request):
    return render_entrypoint(request, "Home", {
        "topText": "Hello!",
        "tagline": {
            "subthing": "keeps going",
            "other": [
                "a", "b", 1234
            ]
        }
    })


def info(request):
    return render(
        request,
        "home/info.html",
        {
            "is_prod": settings.PROD,
            "is_prerelease": settings.PRERELEASE,
            "hostname": socket.gethostname(),
            "consul_host": settings.CONSUL_ADDR,
        },
    )