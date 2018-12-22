# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import models as md

# Create your views here.

def showMain(request):
    field_t = ('host_name','work_ip','map_ip', 'manage_ip', 'store_ip', 'os', 'machine_type',\
               'status', 'in_proj')

    try:
        all_data = md.Hosts.objects.values(*field_t)
    except Exception,e:
        return render(request, 'error.html', {"error":"at hostinfo.views.show_main "+str(e)} )

    row_list=[]
    for i in all_data:
        row = []
        for j in field_t:
            row.append(i.get(j) )
        row_list.append(row)

    return render(request, 'hostinfo/main.html',{'row_list':row_list})




