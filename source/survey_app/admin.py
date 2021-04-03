from django.contrib import admin

# Register your models here.
from survey_app.models import Poll, AnswerOption

admin.site.register(Poll)
admin.site.register(AnswerOption)
