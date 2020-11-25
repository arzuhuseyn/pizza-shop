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