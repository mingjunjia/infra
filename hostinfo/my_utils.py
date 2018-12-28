# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import models as md

def getHostsID(host_name):
    """
    """
    try:
        host_id =  md.Hosts.objects.get(host_name=host_name).id
    except Exception,e:
        return False

    return host_id
    
    
