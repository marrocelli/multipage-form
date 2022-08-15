from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("", views.home, name="home"),
    path("form/", views.form, name="form"),
    path("account/", views.account, name="account"),
]

