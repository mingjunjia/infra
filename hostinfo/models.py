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

    def getDefFields(self):
        rtn = []
        for i in vars(self):
            if i != "_state":
                rtn.append(i)
        return rtn
        

class AccountPasswd(models.Model):
    host_name_id = models.ForeignKey(Hosts, on_delete=models.CASCADE)
    # host_name = models.CharField(max_length=50, unique=True, null=False)
    account_name = models.CharField(max_length=50, null=False)
    account_passwd = models.CharField(max_length=50, null=False)
    account_type = models.CharField(max_length=20, null=False, default="os")
    account_comment = models.CharField(max_length=500, null=True)

    def getDefFields(self):
        rtn = []
        for i in vars(self):
            if i != "_state":
                rtn.append(i)
        return rtn

    class Meta:
       unique_together = ('host_name_id', 'account_name', "account_type")

class HostCap(models.Model):
    host_name_id = models.OneToOneField(Hosts, on_delete=models.CASCADE, default="")
    # host_name = models.CharField(max_length=50, unique=True, null=False)
    cpu_num = models.SmallIntegerField(null=True)
    mem_size = models.SmallIntegerField(null=True)  # G
    rootfs_size = models.SmallIntegerField(null=True)   # G
    disk_desc = models.TextField(null=True, max_length=500)
    nfs_desc = models.TextField(null=True, max_length=500)
    host_comment = models.TextField(null=True, max_length=500)

    def getDefFields(self):
        rtn = []
        for i in vars(self):
            if i != "_state":
                rtn.append(i)
        return rtn

class HWSpec(models.Model):
    host_name_id = models.OneToOneField(Hosts, on_delete=models.CASCADE, default="")
    cpu_spec = models.TextField(null=True, max_length=500)
    mem_spec = models.TextField(null=True, max_length=1000)
    host_model = models.CharField(null=True, max_length=100)
    host_serial_num = models.CharField(null=True, max_length=100)
    host_comment = models.CharField(max_length=500, null=True)

    def getDefFields(self):
        rtn = []
        for i in vars(self):
            if i != "_state":
                rtn.append(i)
        return rtn





