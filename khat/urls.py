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

    path('loginadminF/<str:id_loginad>/<str:pass_login>'
         , views.login_admin.as_view()),
    # Login Admin in new Device WITHOUT send data

    path('loginadminT/<str:id_lo>/<str:pass_lo>', views.login_admin_with_send_data.as_view()),
    # Login Admin in new Device with send data

    path('getstusfromclass/<str:class_pk>', getstus.as_view()),
    # Return List of This class stus

    path('addclassforadmin/<str:admin_pk>/<str:admin_password>'
         '/<str:class_id>/<str:class_name>/<str:class_code>' , views.addClassadmin.as_view())
    # add class for Exist admin
]
