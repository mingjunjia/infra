#coding=utf8
from models import Hosts
from django.shortcuts import render_to_response as response

def insertHosts(request):
    if request.method == "GET":
        return response('hostinfo/host_form.html')

    #1
    if request.POST["host_name"]:
        host_name = request.POST['host_name']
    else:
        return response('hostinfo/host_form.html', {"error":"host_name is required."})
    #2
    if request.POST["work_ip"]:
        work_ip = request.POST["work_ip"]
    else:
        work_ip = ""
    #3
    if request.POST["manage_ip"]:
        manage_ip = request.POST["manage_ip"]
    else:
        manage_ip = ""
    #4
    if "store_ip" in request.POST:
        store_ip = request.POST["store_ip"]
    else:
        store_ip = ""
    #5
    if "map_ip" in request.POST:
        map_ip = request.POST["map_ip"]
    else:
        map_ip = ""
    #6
    if "machine_type" in request.POST:
        machine_type = request.POST["machine_type"]
    else:
        return response('hostinfo/host_form.html', {"error":"machine is required."})
    #7
    if request.POST["in_proj"]:
        in_proj = request.POST["in_proj"]
    else:
        in_proj = ""
    #8
    if "status" in request.POST:
        status = request.POST["status"]
    else:
        return response('hostinfo/host_form.html', {"error":"machine status is required"})
    #9
    if request.POST["os"]:
        os = request.POST["os"]
    else:
        return response('hostinfo/host_form.html', {"error":"machine OS is required"})


    try:
        hosts = Hosts(host_name=host_name, work_ip=work_ip, manage_ip=manage_ip, store_ip=store_ip,\
                      map_ip=map_ip, machine_type=machine_type, in_proj=in_proj, status=status,\
                      os=os)
        hosts.save()
    except Exception,e:
        return response('hostinfo/host_form.html', {"error":e})

    return response('success.html', {"info":"insert data is done."})

