from stories import story, arguments, Success, Result, Failure

from orders.repository import OrderRepository


class UpdateOrderStatus:
    @story
    @arguments('order_id', 'status')
    def run(I):
        I.fetch_order_from_repo
        I.validate_order_status
        I.persist_result

    def fetch_order_from_repo(self, ctx):
        ctx.order = self.repo.get_order(ctx.order_id)
        return Success() if ctx.order else Failure()

    def validate_order_status(self, ctx):
        return Success() if ctx.order.status not in [4,5] else Failure()

    def persist_result(self, ctx):
        ctx.result = self.repo.update_order_status(ctx.order_id, ctx.status)
        return Result(ctx.result)


update_order_status = UpdateOrderStatus()
update_order_status.repo = OrderRepository()