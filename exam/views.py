from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import adminss, classes, imei_admin
from .serializer import sericlassinfo, seristusinfo, serilizermanagerinfo, imeiinfo


# Create your views here.


def registeradmins(request, id_admin, password_admin, name_admin, number_admin):
    s = adminss(id=id_admin, password=password_admin
                , name=name_admin, number=number_admin)
    s.save()
    return HttpResponse("asdsadads", status=status.HTTP_200_OK)


class login_admin(APIView):
    def get(self, request, id_loginad, pass_login , Imei_adminn):

        try:
            adminss.objects.get(pk=id_loginad)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        else:
            if adminss.objects.get(pk=id_loginad).password == pass_login:
                id_ad = adminss.objects.get(pk = id_loginad).id
                pass_ad = adminss.objects.get(pk = id_loginad).password
                imei_admin(imei=Imei_adminn, id_admin=id_ad , pass_admin=pass_ad).save()
                return Response(status=status.HTTP_200_OK)
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


class imei(APIView):
    def get(self, request, imei_adminget):
        try:
            imei_admin.objects.get(pk=imei_adminget)
        except ObjectDoesNotExist:
            Response(status=status.HTTP_304_NOT_MODIFIED)
        else:
            firstlogindata = imei_admin.objects.filter(pk=imei_adminget)
            datas = imeiinfo(firstlogindata, many=True)
            return Response(datas.data)
