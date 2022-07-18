from django.contrib import admin

from . import models
# Register your models here.
class UserLanguagesAdmin(admin.ModelAdmin):
    list_display = ('language_name',)

class LanguageWordsAdmin(admin.ModelAdmin):
    list_display = ('word', 'translation', 'language_name')

admin.site.register(models.UserLanguages, UserLanguagesAdmin)
admin.site.register(models.LanguageWords, LanguageWordsAdmin)
