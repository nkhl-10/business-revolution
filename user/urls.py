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
from django.template.defaulttags import url
from django.urls import path, include
from user import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.home),
                  path('home', views.home),
                  path('about', views.about),
                  path('service', views.service),
                  path('idea', views.idea),
                  path('contact', views.contact),
                  path('feature', views.feature),
                  path('team', views.team),
                  path('testimonial', views.testimonial),
                  path('load', views.load),
                  path('login', views.login),
                  path('logout', views.logout),
                  path('profile', views.profile),
                  path('password', views.password),
                  path('anotherway', views.anotherway),
                  path('readmore/<int:id>', views.readmore),
                  path('user_upload', views.user_upload),
                  path('subscribe2', views.subscribe2),
                  path('search', views.search),
                  path('index', views.index),
                  path('i_save', views.i_save),
                  path('order_payment', views.order_payment),
                  path('callback', views.callback),
                  path('cat/<int:id>/', views.cat),
                  path('view_order', views.view_order),
                  path('buyorder', views.buyorder),
                  path('details1/<int:id>/', views.details1),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
