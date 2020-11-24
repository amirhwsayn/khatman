from rest_framework.views import APIView
from rest_framework.response import Response

from .models import adminss
from django.http import HttpResponse

# Create your views here.
from .serializer import serilizermanagerinfo


def registeradmins(request,id_admin, password_admin, name_admin, number_admin):
    s = adminss(id=id_admin,password=password_admin
                , name=name_admin, number=number_admin)
    s.save()
    return HttpResponse("saved")


class dataadmin(APIView):
    def get(self, request, uuid):
        ret = adminss.objects.filter(pk=uuid)
        seri = serilizermanagerinfo(ret, many=True)
        return Response(seri.data)
