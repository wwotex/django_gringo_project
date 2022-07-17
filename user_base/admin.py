from django.contrib import admin

from . import models
# Register your models here.
class UserLanguagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'n_words_learned')

class LanguageWordAdmin(admin.ModelAdmin):
    list_display = ('word', 'translation')

admin.site.register(models.UserLanguages, UserLanguagesAdmin)
admin.site.register(models.LanguageWordList, LanguageWordAdmin)
