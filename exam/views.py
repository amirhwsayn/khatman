from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import adminss, classes, imei_admin
from .serializer import sericlassinfo, seristusinfo, imeiinfo, serilizermanagerinfo


# Create your views here.


# Rigester Admin
class Rigadmin(APIView):
    def get(self,request, id_admin, password_admin, name_admin, number_admin):

        s = adminss(id=id_admin, password=password_admin
                    , name=name_admin, number=number_admin)
        s.save()
        try:
            adminss.objects.get(pk=id_admin)
        except ObjectDoesNotExist:return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_200_OK)


# Set new IMEI for Exist Admin
class login_admin_at_new_device(APIView):
    def get(self, request, id_loginad, pass_login, Imei_adminnn):
        try:
            adminss.objects.get(pk=id_loginad)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        else:
            if adminss.objects.get(pk=id_loginad).password == pass_login:
                id_ad = adminss.objects.get(pk=id_loginad).id
                pass_ad = adminss.objects.get(pk=id_loginad).password
                imei_admin(imei=Imei_adminnn, id_admin=id_ad, pass_admin=pass_ad).save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)


# return calsss data
class dataclasss(APIView):
    def get(self, request, id_admin, pass_admin):
        if adminss.objects.get(pk=pass_admin).password == pass_admin:
            asd = adminss.objects.get(pk=id_admin).calsss.all()
            data = sericlassinfo(asd, many=True)
            return Response(data.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Return List of This class stus
class getstus(APIView):
    def get(self, request, class_pk):
        ass = classes.objects.get(pk=class_pk).stus_set.all()
        data = seristusinfo(ass, many=True)
        return Response(data.data)


# Return All adminData With IMEI
class return_admindata_W_imei(APIView):
    def get(self, request, imei_adminget):
        try:
            imei_admin.objects.get(pk=imei_adminget)
        except ObjectDoesNotExist:
            Response(status=status.HTTP_304_NOT_MODIFIED)
        else:
            getPKwithimei = imei_admin.objects.get(pk=imei_adminget).id_admin
            dataddd = adminss.objects.filter(pk=getPKwithimei)
            datas = serilizermanagerinfo(dataddd, many=True)
            return Response(datas.data)
