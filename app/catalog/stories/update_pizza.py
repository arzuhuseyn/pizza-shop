from stories import story, arguments, Success, Result, Failure

from catalog.repository import CatalogRepository


class UpdatePizza:
    @story
    @arguments('pk', 'params')
    def run(I):
        I.validate_inputs
        I.persist_result

    def validate_inputs(self, ctx):
        if bool(self.repo.get_pizza(ctx.pk)) and isinstance(ctx.params, dict):
            return Success()
        return Failure()

    def persist_result(self, ctx):
        ctx.result = self.repo.update_pizza(ctx.pk, ctx.params)
        return Result(ctx.result)


update_pizza = UpdatePizza()
update_pizza.repo = CatalogRepository()