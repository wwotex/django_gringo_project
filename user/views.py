from operator import mod
from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import LanguageWords, UserLanguages
from django.views.generic import DetailView,ListView

# Create your views here.
class UserMainView(ListView):
    template_name = 'user/user_languages_list.html'
    model = UserLanguages
    context_object_name = "langs"

class LanguageWordsView(DetailView):
    template_name = 'user/language_word_list.html'
    model = UserLanguages
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        lang_name = context['userlanguages'].language_name
        context['lang_name'] = lang_name.upper()

        list_words = LanguageWords.objects.filter(language_name=lang_name)
        context['word_list'] = list_words
        
        return context