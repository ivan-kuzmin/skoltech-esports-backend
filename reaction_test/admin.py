from django.contrib import admin
from .models import ReactionTestResult


@admin.register(ReactionTestResult)
class ResultAdmin(admin.ModelAdmin):
   list_display = ['user', 'mode', 'success', 'level', 'time_reaction', 'radius', 'created_at']
