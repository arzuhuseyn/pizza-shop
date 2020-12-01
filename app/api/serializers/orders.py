from rest_framework import serializers

from orders.models import OrderProfile, Order, OrderLog
from app.utils.helpers import STATUS_TYPES


class OrderProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProfile
        fields = '__all__'


class OrderProfileWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProfile
        exclude = ['user']


class OrderLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLog
        fields = ['updated_at']


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()
    update_logs = serializers.SerializerMethodField()

    class Meta:
        model = Order
        exclude = ['updated']

    def get_update_logs(self, obj):
        return OrderLogSerializer(obj.update_logs, many=True).data
    
    def get_customer(self, obj):
        return OrderProfileSerializer(obj.customer).data


class OrderStatusSerializer(serializers.ModelSerializer):
    customer = OrderProfileSerializer()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['status', 'customer', 'created_at', 'updated_at']

    def get_status(self, obj):
        return STATUS_TYPES[obj.status][1]