"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from web_test.views import index,login,list,Add,Delete,Update,GET,AssetList


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^index/', index),
    url(r'^login/', login),
    #url(r'^list/(\d*)', list),
    url(r'^list/(?P<id>\d*)/(?P<name>\d*)/', list),
    url(r'^list/(?P<name>\d*)/', list,{'id':222}),
    url(r'^add/(?P<name>\d*)/$', Add),
    url(r'^delete/(?P<name>\d*)/$', Delete),
    url(r'^update/(?P<id>\d*)/(?P<hostname>\w*)/$', Update),
    url(r'^get/(?P<hostname>\w*)/$', GET),
    url(r'^assetlist/$', AssetList),
    
]
