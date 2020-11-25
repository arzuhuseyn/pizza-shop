from django.contrib import admin

from catalog.models import Ingredient, Pizza


admin.site.register(Ingredient)
admin.site.register(Pizza)