import uuid

from django.db import models

from app.utils.abc import BaseModel


class Order(BaseModel):
    STATUS_TYPES = (
        (1, "Accepted"),
        (2, "Preparing"),
        (3, "On the way"),
        (4, "Delivered"),
        (5, "Declined")
    )
    uuid = models.CharField(max_length=40, default=str(uuid.uuid4()))
    customer=models.ForeignKey(
        "orders.OrderProfile",
        verbose_name="Customer",
        on_delete=models.CASCADE
    )
    status=models.IntegerField(choices=STATUS_TYPES, default=1)
    items=models.JSONField(verbose_name="Order items")

    class Meta:
        verbose_name="Order"
        verbose_name_plural="Orders"

    def __str__(self):
        return f"{self.customer} - ORDER NO: {self.uuid}"