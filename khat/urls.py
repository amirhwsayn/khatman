"""khat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from exam import views


urlpatterns = [
    path('admin/', admin.site.urls),

    # admins url
    path('rigstu/<str:id_admin>', views.dataclasss.as_view()),
    path('rigesteradmin/<str:id_admin>/<str:password_admin>'
         '/<str:name_admin>/<str:number_admin>', views.registeradmins),
    path('loginadmin/<str:id_loginad>/<str:pass_login>', views.login_admin.as_view()),
    # end admins url


    path('aaaaa' , views.sttt)
]
