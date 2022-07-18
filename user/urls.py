from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserMainView.as_view(), name='language.list'),
    path('user/<str:pk>', views.LanguageWordsView.as_view(), name='word.list'),
]
