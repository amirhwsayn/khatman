from rest_framework import serializers
from .models import adminss , classes



class serilizermanagerinfo(serializers.ModelSerializer):
    class Meta:
        model = adminss
        fields = [
            'id',
            'password',
            'name',
            'number',
        ]


class sericlassinfo(serializers.ModelSerializer):
    class Meta:
        model = classes
        fields = [
            'id',
            'name',
            'code',
            'datacreate',
        ]