"""weebserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myadmins import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loadfile),
    path('user_data', views.user_data),
    path('invoice', views.invoice),
    path('alert', views.alert),
    path('analytics', views.analytics),
    path('apex', views.apex),
    path('badge', views.badge),
    path('chat', views.chat),
    path('team', views.team),
    path('contacts', views.contacts),
    path('uas', views.uas),
    path('approve', views.approve),
    path('Readmore', views.Readmore),
]
