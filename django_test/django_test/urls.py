"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include

from . import view
from model_test.urls import urlpatterns as model_test_urls
from form_test.urls import urlpatterns as form_test_urls
from rest_model_test.urls import urlpatterns as rest_test_urls
from rest_raw_test.urls import urlpatterns as rest_raw_urls

urlpatterns = [
    re_path(r'^$', view.hello),
    path('hello', view.hello),
    path('raw_api', view.raw_api),
    path('admin/', admin.site.urls),
    path("", include(model_test_urls)),
    path("", include(form_test_urls)),
    path("", include(rest_test_urls)),
    path("", include(rest_raw_urls)),
]
