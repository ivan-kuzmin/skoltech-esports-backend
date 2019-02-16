from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class ReactionTestResult(models.Model):
    success = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    mode = models.CharField(max_length=20)
    level = models.IntegerField()
    time_reaction = models.FloatField()
    radius = models.IntegerField()
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name="Result"
