from stories import story, arguments, Success, Result, Failure

from orders.factories import OrderItemFactory
from orders.repository import OrderRepository
from catalog.repository import CatalogRepository


class UpdateOrderItems:
    @story
    @arguments('order_id', 'items')
    def run(I):
        I.fetch_order_from_repo
        I.validate_order_status
        I.build_items
        I.persist_result

    def fetch_order_from_repo(self, ctx):
        ctx.order = self.repo.get_order(ctx.order_id)
        return Success() if ctx.order else Failure()

    def validate_order_status(self, ctx):
        return Success() if ctx.order.status in [0,1,2] else Failure()

    def build_items(self, ctx):
        ctx.order_items = [self.item_factory(
            item_id=item.get('id'),
            size=item.get('size'),
            count=item.get('count'),
            ingredients=item.get('ingredients')
        ).build() for item in ctx.items]
        return Success()

    def persist_result(self, ctx):
        ctx.result = self.repo.update_order_items(ctx.order_id, ctx.order_items)
        return Result(ctx.result)


update_order_items = UpdateOrderItems()
update_order_items.repo = OrderRepository()
update_order_items.item_factory = OrderItemFactory
update_order_items.item_factory.repo = CatalogRepository()