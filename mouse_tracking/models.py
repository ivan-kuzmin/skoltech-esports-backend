from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from jsonfield import JSONField


class MouseTrackingResult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    trial = models.CharField(max_length=20)
    speed = models.IntegerField()
    radius = models.IntegerField()
    sensitivity = models.FloatField()
    trajectories = JSONField()
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name="Result"
