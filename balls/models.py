from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from jsonfield import JSONField


class Result(models.Model):
    success = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    level = models.IntegerField()
    true_balls = models.IntegerField()
    false_balls = models.IntegerField()
    balls = models.IntegerField()
    red_balls = models.IntegerField()
    speed = models.IntegerField()
    radius = models.IntegerField()
    # red = JSONField()
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
