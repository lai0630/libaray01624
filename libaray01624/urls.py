"""
URL configuration for libaray01624 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from mysite.views import homepage
from mysite import views as mv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
    path('post/<slug:slug>/', mv.showpost, name="showpost"),#slug代表是變數(用<內容就是你在資料庫打的網址名稱>)  如果輸入post/.../就跑去那個函式
    path('login/',mv.log,name="login"),
    path('book_list/', mv.book_list, name='book_list'),
    path('borrow/<int:book_id>/', mv.borrow_book, name='borrow_book'),
    path('return/<int:book_id>/', mv.return_book, name='return_book'),
    path('search/',mv.search,name="search"),
    path('forms/',mv.forms,name='forms')
]
