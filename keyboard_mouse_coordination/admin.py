from django.contrib import admin
from .models import KeyboardMouseCoordinationResult


@admin.register(KeyboardMouseCoordinationResult)
class ResultAdmin(admin.ModelAdmin):
   list_display = ['user', 'trial', 'time', 'hit', 'speed', 'radius', 'balls', 'keyboard_step', 'sensitivity', 'created_at']
