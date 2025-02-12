from django.contrib import admin

from .models import Shipment, LiveUpdate

admin.site.register(Shipment)
admin.site.register(LiveUpdate)
