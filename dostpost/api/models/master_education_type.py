from django.db import models


class MasterEducationType(models.Model):
    education_type = models.CharField(max_length=500, null=True, blank=True)
