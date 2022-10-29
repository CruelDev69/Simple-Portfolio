"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from home import views
from django.views.static import serve
from django.urls import re_path
from django.conf import settings


admin.site.site_header = "Ahad Noor"
admin.site.site_title = "Ahad's Admin Portal"
admin.site.index_title = "Welcome to Ahad's Website"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]