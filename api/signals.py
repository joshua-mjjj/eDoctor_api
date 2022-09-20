from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Client, Property

@receiver(post_save, sender=Property)
def create_client(sender, instance, created, **kwargs):
    check_client = Client.objects.filter(customer_contact=instance.client_contact)

    if created:
        if(check_client.exists() == False):
            Client.objects.create(customer_contact=instance.client_contact,
                              customer_name=instance.client_name,
                              customer_email=instance.client_email)

# @receiver(post_save, sender=Booking)
# def save_client(sender, instance, **kwargs):
#     instance.save()
