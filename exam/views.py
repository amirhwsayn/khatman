from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import adminss, classes
from .serializer import sericlassinfo, seristusinfo, serilizermanagerinfo


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


# login admin without send Admin data
class login_admin(APIView):
    def get(self, request, id_loginad, pass_login):

        # admin object is not exist and must register
        try:
            adminss.objects.get(pk=id_loginad)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        else:
            if adminss.objects.get(pk=id_loginad).password == pass_login:
                # sign admin in device is sucssfull
                return Response(status=status.HTTP_200_OK)

            else:
                # admin password is incorrect
                return Response(status=status.HTTP_400_BAD_REQUEST)


# Login Admin in new Device with send data
class login_admin_with_send_data(APIView):
    def get(self, request, id_lo, pass_lo):

        # admin object is not exist and must register
        try:
            adminss.objects.get(pk=id_lo)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        else:
            if adminss.objects.get(pk=id_lo).password == pass_lo:
                # sign admin in device is sucssfull
                admindata = adminss.objects.filter(pk = id_lo)
                ValidAdminData = serilizermanagerinfo(admindata , many=True).data
                return Response(ValidAdminData , status=status.HTTP_200_OK)

            else:
                # admin password is incorrect
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

