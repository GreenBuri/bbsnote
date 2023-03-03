"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from bbsnote import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bbsnote/', include('bbsnote.urls')), #bbstnote라는 주소로 들어오게 되면, bbsnote아래 urls.py로 보내겠다.
    path('common/', include('common.urls')), # common으로 들어올 경우!(로그인,로그아웃 기능 사용할경우) common.urls.py로 보내도록
    path('',views.index, name='index'), #지금까지는 url에 아무것도 입력하지 않으면 404가 출력되었음. 그걸 방지하기 위함
]

