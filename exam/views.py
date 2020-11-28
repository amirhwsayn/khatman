from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import adminss, classes
from .serializer import sericlassinfo, seristusinfo, serilizermanagerinfo


# Create your views here.


def registeradmins(request, id_admin, password_admin, name_admin, number_admin):
    s = adminss(id=id_admin, password=password_admin
                , name=name_admin, number=number_admin)
    s.save()
    return HttpResponse("asdsadads", status=status.HTTP_200_OK)


class login_admin(APIView):
    def get(self, request, id_loginad, pass_login):
        try:
            adminss.objects.get(pk = id_loginad)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        datas = adminss.objects.get(pk=id_loginad)
        if datas.password == pass_login:
            jsondata = adminss.objects.filter(pk=id_loginad)
            dataserializ = serilizermanagerinfo(jsondata, many=True)
            return Response(dataserializ.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class dataclasss(APIView):
    def get(self, request, id_admin):
        asd = adminss.objects.get(pk=id_admin).calsss.all()
        data = sericlassinfo(asd, many=True)
        return Response(data.data)


class getstus(APIView):
    def get(self, request, class_pk):
        ass = classes.objects.get(pk=class_pk).stus_set.all()
        data = seristusinfo(ass, many=True)
        return Response(data.data)
