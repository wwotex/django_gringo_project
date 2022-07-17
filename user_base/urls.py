from django.urls import path
from . import views

urlpatterns = [
    path('user', views.MainUserPageView.as_view()),
    path('user/lang', views.UserLanguagePageView.as_view()),
]
