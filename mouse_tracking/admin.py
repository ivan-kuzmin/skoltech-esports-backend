from django.contrib import admin
from .models import MouseTrackingResult


@admin.register(MouseTrackingResult)
class ResultAdmin(admin.ModelAdmin):
   list_display = ['user', 'trial', 'speed', 'radius', 'sensitivity', 'trajectories', 'created_at']
