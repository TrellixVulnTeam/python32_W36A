"""django_orm URL Configuration

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
from booksys import views as book_view
#两个应用必须用别名区分

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^query/', views.query),
    
    # 获取所有书籍的路径
    url(r'^books/', book_view.books),
    url(r'^add_book/', book_view.add_book),
    url(r'^edit_book/(\d+)/', book_view.edit_book),
    # http://127.0.0.1:8000/edit_book/2/
    url(r'^del_book/(\d+)/', book_view.del_book),
    # http://127.0.0.1:8000/edit_book/2/
]
