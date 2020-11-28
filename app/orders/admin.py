from django.contrib import admin

from orders.models import OrderProfile, Order, OrderLog

admin.site.register(OrderProfile)
#admin.site.register(Order)
admin.site.register(OrderLog)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'id', 'updated']
    list_editable = ['updated']