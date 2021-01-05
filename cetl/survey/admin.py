from django.contrib import admin

# Register your models here.

from .models import Survey, Question, Response

admin.site.register([Survey, Question, Response])