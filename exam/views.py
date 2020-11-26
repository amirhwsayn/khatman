from django.views.decorators.http import require_http_methods
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import adminss
from django.http import HttpResponse

# Create your views here.
from .serializer import serilizermanagerinfo


def registeradmins(request, id_admin, password_admin, name_admin, number_admin):
    s = adminss(id=id_admin, password=password_admin
                , name=name_admin, number=number_admin)
    s.save()
    return Response(status=status.HTTP_202_ACCEPTED)



class login_admin(APIView):
    def get(self, request, id_loginad , pass_login):
        password = adminss.objects.get(pk=id_loginad).password
        if (password == pass_login):
            data = adminss.objects.filter(pk=id_loginad)
            dataserializ = serilizermanagerinfo(data, many=True)
            return Response(dataserializ.data)
        else:return Response(status=status.HTTP_400_BAD_REQUEST)
