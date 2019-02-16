from django.contrib import admin
from .models import ReactionDecisionTestResult


@admin.register(ReactionDecisionTestResult)
class ResultAdmin(admin.ModelAdmin):
   list_display = ["user", "level", "success", "correct_result", "color", "radius", "x", "y", "width", "height", "time_reaction", "created_at"]
