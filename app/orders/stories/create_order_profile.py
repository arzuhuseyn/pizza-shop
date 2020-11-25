from stories import story, arguments, Success, Result, Failure

from orders.repository import OrderRepository


class CreateOrderProfile:
    @story
    @arguments('user_id', 'params')
    def run(I):
        I.validate_inputs
        I.persist_result

    def validate_inputs(self, ctx):
        for v in ctx.params.values():
            return Failure() if v == None or type(v) != str else Success()

    def persist_result(self, ctx):
        ctx.result = self.repo.create_order_profile(ctx.user_id, ctx.params)
        return Result(ctx.result)


create_order_profile = CreateOrderProfile()
create_order_profile.repo = OrderRepository()