from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from import_export import resources
# from import_export.admin import ImportExportModelAdmin

from api.models import (
    User,
    Property,
    Client,
    Appointment
)

admin.site.site_header = "eDoctor"
admin.site.index_title = "Admin Dashboard"

class PropertyAdmin(admin.ModelAdmin):
    list_display = ["client_contact", "client_name", "property_type", "property_location", "property_booked", "price", "verified", "owner"]

class ClientAdmin(admin.ModelAdmin):
    list_display = ["customer_contact", "customer_name", "customer_email", "created_at"]

admin.site.register(User)
admin.site.register(Appointment)

# customer_contact = models.CharField(max_length=52)
#     customer_name = models.CharField(max_length=52, blank=True, null=True)
#     customer_email = models.CharField(max_length=52, blank=True, null=True)
#     booking_type = models.CharField(max_length=52, choices=BOOKING_TYPES)
#     venue = models.CharField(max_length=152) # FAST SPORTS FUSION UG
#     court_location = models.CharField(max_length=52, choices=COURT_TYPES)
#     start_date = models.DateField()
#     end_date = models.DateField(blank=True, null=True)
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     duration = models.CharField(max_length=102)
#     block_booking = models.BooleanField(default=False)
#     cost = models.IntegerField(blank=True, null=True)
#     blocked_off = models.BooleanField(default=False)