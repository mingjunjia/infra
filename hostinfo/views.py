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

def updateHost(request):
    if request.method == "GET":
        return render(request, "hostinfo/update_host.html")

    if "host_name" in request.POST and request.POST["host_name"] != '':
        if len( md.Hosts.objects.filter(host_name=request.POST["host_name"])) == 0:
            notify = "no update data: the host not exist, please fore insert."
            return render(request, "hostinfo/update_host.html", {"status":notify} )

        field_l = ['work_ip','map_ip', 'manage_ip', 'store_ip', 'os', 'machine_type',\
               'status', 'in_proj']
        try:
            for i in field_l:
                   if (i not in request.POST) or request.POST[i] == "":
                       field_l.remove(i)
            field_d = {}

            for i in field_l:
                field_d.update( { i:request.POST[i] } )

            md.Hosts.objects.filter(host_name=request.POST["host_name"]).update(**field_d)
        except Exception,e:
               return render(request, "hostinfo/update_host.html", {"error":"hostinfo/views \
                                                                    updateHost:" + str(e)} )
        return render(request, "hostinfo/update_host.html",{"status":"success update."})


    else:
        return render(request, "hostinfo/update_host.html",{"status":"host name is required"})


def deleteHost(request):
    if request.method == "GET":
        return render(request, "hostinfo/update_host.html")

    if "host_name" in request.POST and request.POST["host_name"] != '':
        if len( md.Hosts.objects.filter(host_name=request.POST["host_name"])) == 0:
            notify = "no update data: the host not exist, please fore insert."
            return render(request, "hostinfo/update_host.html", {"status":notify} )

    try:
        host = md.Hosts.objects.get(host_name=request.POST['host_name'])
        host.delete()
    except Exception,e:

        return render(request, "hostinfo/update_host.html", {"error":"hostinfo/views \
                                                             deleteHost: failed +"+ str(e)})
