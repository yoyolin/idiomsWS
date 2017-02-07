from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Idioms(models.Model):
    idiom = models.CharField(max_length = 200);
    level = models.IntegerField();

    def __str__(self):              # __unicode__ on Python 2
        return self.idiom