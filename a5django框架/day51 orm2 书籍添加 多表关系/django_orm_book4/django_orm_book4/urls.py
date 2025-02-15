"""django_orm_book4 URL Configuration

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

from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^query/', views.query),  #添加数据
	
    url(r'^books/', views.books),  #图书列表展示
    url(r'^add_book/', views.add_book),  #添加图书
    url(r'^edit_book/(\d+)/', views.edit_book),  #编辑图书
    url(r'^del_book/(\d+)/', views.del_book),  #删除图书
]
