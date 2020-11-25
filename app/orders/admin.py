from django.contrib import admin

from orders.models import OrderProfile, Order

admin.site.register(OrderProfile)
admin.site.register(Order)