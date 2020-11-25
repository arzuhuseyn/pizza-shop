from stories import story, arguments, Success, Result, Failure

from orders.repository import OrderRepository


class CreateOrder:
    @story
    @arguments('customer', 'items')
    def run(I):
        I.validate_inputs
        I.persist_result

    def validate_inputs(self, ctx):
        return Success()

    def persist_result(self, ctx):
        ctx.result = self.repo.create_order(ctx.customer, ctx.items)
        return Result(ctx.result)


create_order = CreateOrder()
create_order.repo = OrderRepository()