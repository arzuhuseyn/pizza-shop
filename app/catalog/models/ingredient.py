from django.db import models
from app.utils.abc import BaseModel


class Ingredient(BaseModel):
    name = models.CharField(
        max_length=50,
        verbose_name="Ingredient name"
    )

    class Meta:
        verbose_name="Ingredient"
        verbose_name_plural="Ingredients"

    def __str__(self):
        return self.name