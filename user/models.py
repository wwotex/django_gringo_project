from django.db import models

# Create your models here.
class UserLanguages(models.Model):
    language_name = models.CharField(max_length=20, primary_key=True)
    # n_words_learned = models.PositiveIntegerField()

class LanguageWords(models.Model):
    language_name = models.ForeignKey(UserLanguages, on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    translation = models.CharField(max_length=50)
    time_created = models.DateTimeField(auto_now_add=True)