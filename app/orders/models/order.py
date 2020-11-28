from django.db import models

from app.utils.abc import BaseModel
from app.utils.helpers import STATUS_TYPES

class Order(BaseModel):
    customer=models.ForeignKey(
        "orders.OrderProfile",
        verbose_name="Customer",
        on_delete=models.CASCADE
    )
    status=models.IntegerField(choices=STATUS_TYPES, default=0)
    items=models.JSONField(verbose_name="Order items")
    updated=models.BooleanField(default=False)

    class Meta:
        verbose_name="Order"
        verbose_name_plural="Orders"

    def __str__(self):
        return f"{self.customer} - ORDER NO: {self.id}"
    
    def save(self, *args, **kwargs):
        if self.updated:
            self.status=0
            self.updated=False
        return super().save(*args, **kwargs)



class OrderLog(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="update_logs")

    class Meta:
        verbose_name="Order Log"
        verbose_name_plural="Order Logs"

    def __str__(self):
        return f"OrderLog - {self.order.id}"