from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from rest_framework.response import Response

from api.serializers import IngredientSerializer, PizzaSerializer
from catalog.repository import CatalogRepository


catalog_repo = CatalogRepository()


class PizzaListAPIView(ListAPIView):
    serializer_class = PizzaSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return catalog_repo.list_pizzas()


class IngredientListAPIView(ListAPIView):
    serializer_class = IngredientSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return catalog_repo.list_ingredients()