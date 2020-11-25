from django.db import models
from django.contrib.auth import get_user_model

from app.utils.abc import BaseModel


User = get_user_model()


class OrderProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=80, verbose_name="Customer name")
    surname = models.CharField(max_length=80, verbose_name="Customer surname")
    address = models.TextField(verbose_name="Customer address")
    phone = models.CharField(max_length=30, verbose_name="Customer contact number")

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.user.__str__() if self.user else f"{self.name} {self.surname}"
