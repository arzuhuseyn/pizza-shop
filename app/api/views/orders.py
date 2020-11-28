from typing import List
from django.db.models import query
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView
)

from app.utils.decorators import handle_err

from api.serializers import (
    OrderProfileSerializer,
    OrderSerializer,
    OrderStatusSerializer
)

from orders.models import OrderProfile, Order
from orders.repository import OrderRepository
from orders.stories import create_order, update_order_items, update_order_status

order_repo = OrderRepository()


class OrderProfileAPIView(APIView):
    serializer_class = OrderProfileSerializer
    permission_classes =[permissions.AllowAny]

    @handle_err
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serializer = self.serializer_class(
            order_repo.get_order_profile(pk)
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderListAPIView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = order_repo.list_orders()
        params = self.request.query_params
        if params.get('customer_id'):
            qs = qs.filter(customer_id=params.get('customer_id'))
        if params.get('status'):
            qs = qs.filter(status=params.get('status'))
        return qs


class CreateOrderAPIView(APIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

    #@handle_err
    def post(self, request, *args, **kwargs):
        result = create_order.run(
            customer=request.data.get('customer_id'),
            items = request.data.get('items')
        )
        serializer = self.serializer_class(result)
        return Response(serializer.data)


class OrderAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes =[permissions.AllowAny]
    queryset=Order.objects.all()

    @handle_err
    def put(self, request, *args, **kwargs):
        result = update_order_items.run(
            order_id=self.get_object().id,
            items=request.data.get('items')
        )
        serializer=self.serializer_class(result)
        return Response(serializer.data)


class UpdateOrderStatusAPIView(RetrieveUpdateAPIView):
    serializer_class = OrderStatusSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Order.objects.all()

    @handle_err
    def put(self, request, *args, **kwargs):
        result = update_order_status.run(
            order_id=self.get_object().id,
            status=request.data.get('status')
        )
        serializer=self.serializer_class(result)
        return Response(serializer.data)