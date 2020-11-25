from django.db import models
from django.contrib.postgres.fields import ArrayField
from app.utils.abc import BaseModel


class Pizza(BaseModel):
    name = models.CharField(max_length=60, verbose_name="Name of the Pizza")
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = "Pizza"
        verbose_name_plural = "Pizzas"

    def choice_size(self, v=None):
        sizes = {
            's' : 'Small',
            'm' : 'Medium',
            'l' : 'Large'
        }
        return sizes.get(v) if sizes.get(v) else None

    def __str__(self):
        return self.name 