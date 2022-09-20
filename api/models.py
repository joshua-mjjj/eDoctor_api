import binascii
import os

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Avg
from model_utils.models import TimeStampedModel
from rest_framework_jwt.settings import api_settings

ACCOUNT_TYPES = (
    ("Patient", "Patient"),
    ("Doctor", "Doctor"),
)

PROPERTY_TYPES = (
    ("Apartment", "Apartment"),
    ("Rental", "Rental"),
    ("Hostel", "Hostel"),
    ("Motel", "Motel"),
    ("Retail Shop Space", "Retail Shop Space")
)

VERIFIED_STATUS = (
    ("Pending", "Pending"),
    ("Accepted", "Accepted"),
    ("Rejected", "Rejected"),
)

class UserManager(BaseUserManager):
    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        # email = self.normalize_email(email)
        is_active = extra_fields.pop("is_active", True)
        user = self.model(
            username=username,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        is_staff = extra_fields.pop("is_staff", False)
        return self._create_user(username, password, is_staff, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, True, True, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True) # db_index=True
    email = models.EmailField(
        "email address", max_length=255, unique=False, blank=True, null=True
    )
    account_type = models.CharField(max_length=32, choices=ACCOUNT_TYPES)
    
    hospital = models.CharField(max_length=32, blank=True, null=True)
    first_name = models.CharField(max_length=32, default="", blank=True, null=True)
    last_name = models.CharField(max_length=32, default="", blank=True, null=True)
    speciality = models.CharField(max_length=32, blank=True, null=True)
    age = models.CharField(max_length=32, blank=True, null=True)
    weight = models.CharField(max_length=32, blank=True, null=True)
    location = models.CharField(max_length=32, blank=True, null=True)
    patient_problem = models.CharField(max_length=32, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True) # null=True


    is_staff = models.BooleanField("staff status", default=False)
    is_active = models.BooleanField("active", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "username" # Making username the required field
    REQUIRED_FIELDS = []

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(self)
        token = jwt_encode_handler(payload)

        return token

def generate_password_reset_code():
    return binascii.hexlify(os.urandom(20)).decode("utf-8")

# Appointment 
class Appointment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="doctor")
    patient = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="patient")
    patient_sickness = models.CharField(max_length=102, blank=True, null=True)
    description = models.CharField(max_length=102, blank=True, null=True)
    symptoms = models.CharField(max_length=102, blank=True, null=True)
    start_date  = models.DateField(auto_now_add=True, blank=True, null=True)
    start_time = models.TimeField(auto_now_add=True, blank=True, null=True)
    end_time = models.TimeField(auto_now_add=True, blank=True, null=True)
    verified_status =  models.CharField(max_length=52, choices=VERIFIED_STATUS)

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"

    def __str__(self):
        return '{}'.format(self.start_date)


# Booking 
class Property(models.Model):
    client_contact = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100, blank=True, null=True)
    client_email = models.CharField(max_length=100, blank=True, null=True)
    property_name = models.CharField(max_length=100, blank=True, null=True)
    property_type = models.CharField(max_length=52, choices=PROPERTY_TYPES)
    property_location = models.CharField(max_length=152, help_text="Where is the property located ?") 
    property_description = models.CharField(max_length=200, blank=True, null=True)
    
    property_booked = models.BooleanField(default=False, help_text="Has the property been booked or taken ?")
    price = models.IntegerField(blank=True, null=True)
    verified = models.BooleanField(default=False, help_text="Has the property been verified by admins ?")
    verified_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    send_property_verification_email = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    partial_payment = models.BooleanField(default=False, help_text="Do you accept partial/installments mode of payment ?")
    additional_info = models.CharField(max_length=100, blank=True, null=True, help_text="Any more additional info or specifics about the property ?")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="property_owner")


    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self):
        return '{}'.format(self.client_name)

# Booking 
class Client(models.Model):
    customer_contact = models.CharField(max_length=52)
    customer_name = models.CharField(max_length=52, blank=True, null=True)
    customer_email = models.CharField(max_length=52, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return '{}, {}'.format(self.customer_name, self.customer_contact)




