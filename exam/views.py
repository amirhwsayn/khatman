from django.views.decorators.http import require_http_methods
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import adminss, stus, classes
from django.http import HttpResponse
from .serializer import serilizermanagerinfo, sericlassinfo


# Create your views here.


def registeradmins(request, id_admin, password_admin, name_admin, number_admin):
    s = adminss(id=id_admin, password=password_admin
                , name=name_admin, number=number_admin)
    s.save()
    return HttpResponse("asdsadads", status=status.HTTP_200_OK)


class login_admin(APIView):
    def get(self, request, id_loginad, pass_login):
        password = adminss.objects.get(pk=id_loginad).password
        if password == pass_login:
            data = adminss.objects.filter(pk=id_loginad)
            dataserializ = serilizermanagerinfo(data, many=True)
            return Response(dataserializ.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class dataclasss(APIView):
    def get(self, request, id_admin):
        asd = adminss.objects.get(pk=id_admin).calsss.all()
        data = sericlassinfo(asd, many=True)
        return Response(data.data)


def sttt(request):
    ass = classes.objects.get(pk = 'ahamd').stus_set.all()
    return HttpResponse(ass)
