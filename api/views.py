import datetime
import hashlib
import json
import os
import random

from rest_framework import status, serializers
from rest_framework.generics import GenericAPIView, ListAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework_jwt.views import ObtainJSONWebToken
from django.core.paginator import Paginator 
from django.http import JsonResponse, HttpResponse 

from ubook_backend.settings import unique_token

from api.models import *
from api.serializers import *
from .email import send__email


class AccountLoginAPIView(ObtainJSONWebToken):
    serializer_class = JWTSerializer

class SignUp(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # user.is_active = False
            user.set_password(serializer.validated_data["password"])
            user.save()

            username = serializer.data["username"]

            # Get user by username
            user = User.objects.get(username=username)

            return Response(
                UserSerializer(user, many=False).data, status=status.HTTP_200_OK
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfile(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def perform_create(self, serializer):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=kwargs.get('pk'))
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        return Response(serializer.data)

class PropertyViewset(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = PropertySerializer
    queryset = Property.objects.all()

    def partial_update(self, request, *args, **kwargs):
        print("Updating...")
        instance = self.queryset.get(pk=kwargs.get('pk'))

        initial_state = self.serializer_class(instance)
        initial_verified_status = initial_state.data["blocked_off"]
        initial_verified_status = initial_state.data["blocked_off"]

        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        new_verified_status = request.data['blocked_off']
        serializer.save()

        email_object = {
             "initial_verified_status": initial_verified_status,
             "new_verified_status": new_verified_status,
             "customer_name": serializer.data["customer_name"],
             "customer_email": serializer.data["customer_email"],
             "booking_type": serializer.data["booking_type"],
             "court_location": serializer.data["court_location"],
             "start_date": serializer.data["start_date"],
             "end_date": serializer.data["end_date"],
             "start_time": serializer.data["start_time"],
             "end_time": serializer.data["end_time"],
             "duration": serializer.data["duration"],
             "cost": serializer.data["cost"],
             "verified_by": serializer.data["verified_by"],
             "send_verification_email": serializer.data["send_verification_email"],
        }

        send__email(email_object)
        return Response(serializer.data)

class ClientsViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ClientsSerializer
    queryset = Client.objects.all()

class AppointmentViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all() 

class ChangePasswordApi(GenericAPIView):
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data["old_password"]
            new_password = serializer.data["new_password"]

            user = self.request.user

            if not user.check_password(old_password):
                content = {"detail": "Invalid Password"}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            else:
                user.set_password(new_password)
                user.save()
                content = {"success": "Password Changed"}
                return Response(content, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

