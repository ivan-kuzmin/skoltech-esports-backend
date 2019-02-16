from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class ReactionDecisionTestResult(models.Model):
    success = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    level = models.IntegerField()
    correct_result = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    radius = models.IntegerField()
    x = models.FloatField()
    y = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    time_reaction = models.FloatField()
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name="Result"
