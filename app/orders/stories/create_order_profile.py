from stories import story, arguments, Success, Result, Failure

from orders.repository import OrderRepository


class CreateOrderProfile:
    @story
    @arguments('user_id', 'params')
    def run(I):
        I.validate_inputs
        I.persist_result

    def validate_inputs(self, ctx):
        i = all(isinstance(v, str) for v in ctx.params.values())
        return Success() # if i else Failure()

    def persist_result(self, ctx):
        ctx.result = self.repo.create_order_profile(ctx.user_id, ctx.params)
        return Result(ctx.result)


create_order_profile = CreateOrderProfile()
create_order_profile.repo = OrderRepository()