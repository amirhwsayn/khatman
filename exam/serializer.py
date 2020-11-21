from rest_framework import serializers
from .models import adminss



class serilizermanagerinfo(serializers.ModelSerializer):
    class Meta:
        model = adminss
        fields = (
            'id',
            'password',
            'name',
            'namesc',
            'number',
        )