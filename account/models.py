from django.db import models
from . import constants

class Shipment(models.Model):
    sender_name = models.CharField(max_length=150)
    sender_email = models.EmailField()
    sender_phone = models.CharField(max_length=20)
    sender_address = models.CharField(max_length=200)

    receiver_name = models.CharField(max_length=150)
    receiver_email = models.EmailField()
    receiver_phone = models.CharField(max_length=20)
    receiver_address = models.CharField(max_length=200)

    tracking_number = models.CharField(max_length=100, unique=True)
    weight = models.CharField(max_length=50)
    content = models.CharField(max_length=400)
    shipping_type = models.CharField(max_length=100)
    origin_office = models.CharField(max_length=100)
    destination_office = models.CharField(max_length=100)
    shipping_date = models.DateField()
    delivery_date = models.DateField()
    booking_mode = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.sender_name


class LiveUpdate(models.Model):
    shipment = models.ForeignKey(Shipment, related_name='live_update', on_delete=models.CASCADE)
    # current_location = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    remark = models.CharField(max_length=500, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    stages_status = models.CharField(max_length=50, choices=constants.STATES_LIVE_CHOICES)
    stages_label = models.CharField(max_length=50, choices=constants.STATES_LABEL_CHOICES)

    def __str__(self):
        return self.status
