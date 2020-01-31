from django.db import models
from jsonfield import JSONField

# Create your models here.
class Activity(models.Model):
    ACTIVITY_ID = models.IntegerField(null=True)
    ACC_X = JSONField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

