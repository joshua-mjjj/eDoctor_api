from __future__ import division

import datetime

from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer

from api.models import *

class JWTSerializer(JSONWebTokenSerializer):
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        update_last_login(None, validated_data["user"])
        return validated_data

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username", "account_type", "password",
            "hospital", "speciality", "age", "weight", "location",
            "patient_problem", "contact")

class UserSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        rep = super(UserSerializer, self).to_representation(instance)
        rep.pop("password", None)
        return rep

    class Meta:
        model = User
        fields = "__all__"
        write_only_fields = ("password",)

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=120)
    new_password = serializers.CharField(max_length=120)

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
