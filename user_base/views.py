from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class MainUserPageView(TemplateView):
    template_name = 'user/user_main.html'

class UserLanguagePageView(TemplateView):
    template_name = 'user/lang/user_language_page.html'