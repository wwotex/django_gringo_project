from django.urls import path

from . import views

urlpatterns = [
    path('', views.LoginPageView.as_view())
]