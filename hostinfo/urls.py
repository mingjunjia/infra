"""infra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import insert
import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'insert/', insert.insertHosts),
    url(r'main/', views.showMain),
    url(r'update/', views.updateHost),
    url(r'delete/', views.deleteHost),
    url(r'detail/', views.showHost),
    url(r'addaccount/', views.addAccount),
    url(r'upaccount/', views.updateAccount),
    url(r'delaccount/', views.deleteAccount),
    url(r'addcap/', views.addHostCap),
    url(r'upcap/', views.updateHostCap),
    url(r'delcap/', views.deleteHostCap),
    url(r'addhw/', views.addHWSpec),
    url(r'uphw/', views.updateHWSpec),
    url(r'delhw/', views.deleteHWSpec),

]
