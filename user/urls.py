from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserMainView.as_view()),
    path('user/<str:pk>', views.LanguageWordsView.as_view()),
]
