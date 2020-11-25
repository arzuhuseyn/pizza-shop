from stories import story, arguments, Success, Result, Failure

from catalog.repository import CatalogRepository


class CreatePizza:
    @story
    @arguments('name', 'size', 'image')
    def run(I):
        I.validate_inputs
        I.persist_result

    def validate_inputs(self, ctx):
        if isinstance(ctx.name, str) and len(ctx.name) < 50 and isinstance(ctx.size, int):
            return Success()
        return Failure()

    def persist_result(self, ctx):
        ctx.params = {
            'name' : ctx.name,
            'size' : ctx.size,
            'image': ctx.image
        }
        ctx.result = self.repo.create_pizza(ctx.params)
        return Result(ctx.result)


create_pizza = CreatePizza()
create_pizza.repo = CatalogRepository()