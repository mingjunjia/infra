# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import models as md
import my_utils as my

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
            notify = "no delete data: the host not exist, please fore insert."
            return render(request, "hostinfo/update_host.html", {"status":notify} )

        try:
            host = md.Hosts.objects.get(host_name=request.POST['host_name'])
            host.delete()
        except Exception,e:
            return render(request, "hostinfo/update_host.html", {"error":"hostinfo/views \
                                                                 deleteHost: failed +"+ str(e)})
    else:
        return render(request, "hostinfo/update_host.html",{"status":"host name is required"})


def showHost(request):
    if request.method != "GET":
        return render(request,"error.html",{"error":"the html method should be GET"})

    if "host_name" not in request.GET:
         return render(request,"error.html",{"error":"the Host Name is required. please try again."})
    
    # make sure the host must exist
    if len( md.Hosts.objects.filter(host_name=request.GET["host_name"])) == 0:
        notify = "the host not exist, please input correct host name."
        return render(request, "error.html", {"status":notify} )

    h1 = md.Hosts.objects.filter(host_name=request.GET["host_name"])[0]
    fields_l = h1.getDefFields()
    fields_val = {}
    for i in fields_l:
        try:    
            fields_val.update( { i:getattr(h1,i) } )
        except Exception,e:
            return render(request,"error.html",{"error":"get field value failed."+ str(e) } )

    return render(request, "hostinfo/host_detail.html", fields_val)
        
    
def addAccount(request):
    if request.method == "GET":
        return render(request, "hostinfo/add_account_form.html")

    if "host_name"  not in request.POST or request.POST["host_name"] == "":
        return render(request, "hostinfo/add_account_form.html", {"status":"Host Name is required, please try again."})

    # h1 = md.accountPasswd()
    fields_l =  ["account_name", "account_passwd", "account_type"]   #h1.getDefFields().remove("host_name_id")
    # fields_l.remove("id")

    tmp_d = {}

    for i in fields_l:
        if i in request.POST and request.POST[i] != "":
            tmp_d.update({i:request.POST[i]})
        else:
            return render(request, "hostinfo/add_account_form.html",{"status":"failed, account name and password is required."})


    try:
        host_id = md.Hosts.objects.get(host_name = request.POST["host_name"])
    except Exception,e:
        return render(request, "hostinfo/add_account_form.html", {"status":"failed: the host no exist in table hostinfo_hosts."+str(e)})
    
    tmp_d.update({"host_name_id":host_id})

    try:
        h2 = md.AccountPasswd(**tmp_d)
        h2.save()
    except Exception,e:
        return render(request, "hostinfo/add_account_form.html", {"status":"Failed,"+ str(e)} )

    return render(request, "hostinfo/add_account_form.html", {"status":"Success insert."})


def updateAccount(request):
    if request.method == "GET":
        return render(request, "hostinfo/account_passwd_form.html")

    fields_l =  ["account_name", "host_name", "account_type"]
    fields_d = {}

    for i in fields_l:
        if i not in request.POST or request.POST[i] == "":
            return render(request, "hostinfo/account_passwd_form.html", {"status": "Host Name and account Name and account Type is required."})
        else:
            fields_d.update({i:request.POST[i]})

    if my.getHostsID(fields_d["host_name"]):
        old_host_id = my.getHostsID(fields_d["host_name"])
        del(fields_d["host_name"])
        fields_d.update({"host_name_id":old_host_id})
    else:
        return render(request, "hostinfo/account_passwd_form.html", {"status": "Host not exist."})



    cnt = 0
    update_fields_d = {}
    fields_l =  ["new_account_name", "new_host_name", "new_account_type", "new_account_passwd", "new_account_comment"]
    for j in fields_l:
        if j in request.POST and request.POST[j] != "":
            cnt = cnt + 1
            update_fields_d.update({j[4:]:request.POST[j]})
    
    if cnt == 0:
        return render(request, "hostinfo/account_passwd_form.html", {"status":"nothing to update, not fields"})

    if "host_name" in update_fields_d:
        try:
            host_id = md.Hosts.objects.get(host_name = update_fields_d["host_name"])
            del(update_fields_d["host_name"])
            update_fields_d.update({"host_name_id":host_id})
        except Exception,e:
            return render(request, "hostinfo/account_passwd_form.html", {"status":"Failed, the host not exist on hosts: "+ str(e)})

    try:
        md.accountPasswd.objects.filter(**fields_d).update(**update_fields_d)
    except Exception,e:
        return render(request, "hostinfo/account_passwd_form.html", {"status": "update Failed : "+str(e)})
    
    return render(request, "hostinfo/account_passwd_form.html", {"status": "Success update."})