"""djjj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import include, path
from . import views
from article import views

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^1/', views.basic_one, name='basic_one'),
    url(r'^2/', views.template_one, name='template_one'),
    url(r'^3/', views.template_two_simple, name='template_two_simple'),
    # url(r'^index/all/', views.ind, name='ind'),
    url('index/get/(?P<article_id>\d+)/$', views.art, name='art'),
    url('^', views.ind, name='ind'),
]