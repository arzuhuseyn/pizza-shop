from django.shortcuts import get_object_or_404

from catalog.models import Ingredient, Pizza


class CatalogRepository:
    """ Persistance layer for the catalog app """

    def create_ingredient(self, name):
        obj, created = Ingredient.objects.get_or_create(
            name = name
        )
        return obj

    def create_pizza(self, params):
        obj = Pizza.objects.create(**params)
        return obj

    def update_pizza(self, pk, params):
        return Pizza.objects.filter(pk=pk).update(**params)

    def update_ingredient(self, pk, name):
        return Ingredient.objects.filter(pk=pk).update(name=name)

    def delete_pizza(self, pk):
        return self.get_pizza(pk=pk).delete()

    def delete_ingredient(self, pk):
        return self.get_ingredient(pk=pk).delete()

    def get_pizza(self, pk=None, name=None):
        if pk:
            return Pizza.objects.filter(pk=pk).first()
        return Pizza.objects.filter(name=name).first()

    def get_ingredient(self, pk=None, name=None):
        if pk:
            return Ingredient.objects.filter(pk=pk).first()
        return Ingredient.objects.filter(name=name).first()

    def list_pizzas(self):
        return Pizza.objects.all()

    def list_ingredients(self):
        return Ingredient.objects.all()

    def get_pizzas_by_id(self, ids):
        return Pizza.objects.filter(id__in=ids)

    def get_ingredients_by_id(self, ids):
        return Ingredient.objects.filter(id__in=ids)