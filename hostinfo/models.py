# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hosts(models.Model):
    host_name = models.CharField(max_length=100, unique=True, null=False)
    work_ip = models.CharField(max_length=30, null=True)
    manage_ip = models.CharField(max_length=30, null=True)
    store_ip = models.CharField(max_length=30, null=True)
    map_ip = models.CharField(max_length=30, null=True)
    os = models.CharField(max_length=20, null=False)
    machine_type = models.CharField(max_length=15, null=False)
    in_proj = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=20, null=False)

