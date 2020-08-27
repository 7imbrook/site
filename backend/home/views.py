import socket, random

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from utils.react import render_entrypoint
from home.models import Page, SlugLocations


def home(request):
    slug = Page.objects.get(type=SlugLocations.HOME)
    messages = slug.slugmessage_set.filter(active=True)
    tagline = random.choice(messages)

    return render_entrypoint(request, "Home", {
        "tagline": tagline.slug
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


def notFound(request, _exception):
    return render_entrypoint(request, "NotFound", {}, status=404)

def somethingWrong(request):
    print("hi?")
    return render_entrypoint(request, "NotFound", {}, status=500)