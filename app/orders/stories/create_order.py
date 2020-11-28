from stories import story, arguments, Success, Result, Failure

from orders.factories import OrderItemFactory
from orders.repository import OrderRepository
from catalog.repository import CatalogRepository


class CreateOrder:
    @story
    @arguments('customer', 'items')
    def run(I):
        I.validate_inputs
        I.build_items
        I.persist_result

    def validate_inputs(self, ctx):
        return Success() if isinstance(ctx.customer, int) and isinstance(ctx.items, list) else Failure()

    def build_items(self, ctx):
        ctx.order_items = [self.item_factory(
            item_id=item.get('id'),
            size=item.get('size'),
            count=item.get('count'),
            ingredients=item.get('ingredients')
        ).build() for item in ctx.items]
        return Success()

    def persist_result(self, ctx):
        ctx.result = self.repo.create_order(ctx.customer, ctx.order_items)
        return Result(ctx.result)


create_order = CreateOrder()
create_order.repo = OrderRepository()
create_order.item_factory = OrderItemFactory
create_order.item_factory.repo = CatalogRepository()