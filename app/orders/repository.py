from orders.models import OrderProfile, Order 


class OrderRepository:

    def create_order_profile(self, user_id, params):
        if user_id:
            params.update({'user_id': user_id})
        obj, created = OrderProfile.objects.get_or_create(**params)
        return obj

    def create_order(self, customer_id, items):
        obj = Order.objects.create(customer_id=customer_id, items=items)
        return obj

    def update_order_items(self, order_id, items):
        obj = self.get_order(order_id)
        obj.items = items
        obj.updated = True
        obj.save()
        return obj

    def update_order_status(self, order_id, status):
        obj = self.get_order(order_id)
        obj.status=status
        obj.save()
        return obj

    def get_order_profile(self, pk):
        return OrderProfile.objects.get(pk=pk)

    def get_order(self, id):
        return Order.objects.get(id=id)

    def get_order_by_id(self, id):
        return Order.objects.get(id=id)

    def list_orders(self):
        return Order.objects.all()