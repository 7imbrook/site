"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import home
from django.contrib import admin
from django.urls import path, include
from django.urls import include, path
from rest_framework import routers
from projects.api.views import ProjectViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    # Pages
    path('', include('home.urls')),
    path('admin/', admin.site.urls),

    # API Paths
    path('api/auth/', include('authorization.api_urls')),
    path('api/projects/', include('projects.api.urls')),

    # Router based routes
    path('api/data/', include(router.urls)),
]

handler404 = home.views.notFound
handler500 = home.views.somethingWrong