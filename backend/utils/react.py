import ujson
from django.shortcuts import render


def render_entrypoint(request, entrypoint, props):
    return render(
        request,
        "home/react-root.html",
        {
            "title": entrypoint,
            "entrypoint": f"{entrypoint}.entrypoint.js",
            "initData": ujson.dumps(props),
        },
    )

