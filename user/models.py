from django.db import models

# Create your models here.
class UserLanguages(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    n_words_learned = models.PositiveIntegerField()

class LanguageWords(models.Model):
    word = models.CharField(max_length=50)
    translation = models.CharField(max_length=50)
    time_created = models.DateTimeField(auto_now_add=True)