from django.db import models


class Profiles(models.Model):
    full_name = models.CharField(max_length=255, null=False, blank=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
