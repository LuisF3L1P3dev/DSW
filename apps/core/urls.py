from django.urls import path

from . views import index, login, base

urlpatterns = [
    path('', index, name="index"),
    path("login/", login, name="login"),
    path("base/", base, name='base'),
]
