from django.contrib import admin
from .models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
   list_display = ['id', 'user', 'success', 'level', 'true_balls', 'false_balls', 'balls', 'speed', 'red_balls', 'radius', 'created_at']
