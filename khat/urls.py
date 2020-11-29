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
from exam.views import getstus

urlpatterns = [
    path('admin/', admin.site.urls),

    path('dataclass/<str:id_admin>/<str:pass_admin>', views.dataclasss.as_view()),
    # return calsss data

    path('rigesteradmin/<str:id_admin>/<str:password_admin>'
         '/<str:name_admin>/<str:number_admin>', views.Rigadmin.as_view()),
    # Rigester Admin

    path('loginadmin/<str:id_loginad>/<str:pass_login>/<str:Imei_adminnn>'
         , views.login_admin_at_new_device.as_view()),
    # Set new IMEI for Exist Admin

    path('getstusfromclass/<str:class_pk>', getstus.as_view()),
    # Return List of This class stus

    path('getalladmindata/<str:imei_adminget>', views.return_admindata_W_imei.as_view()),
    # Return All adminData With IMEI

]
