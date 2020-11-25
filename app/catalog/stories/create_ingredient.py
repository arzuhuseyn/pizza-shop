from stories import story, arguments, Success, Result, Failure

from catalog.repository import CatalogRepository


class CreateIngredient:
    @story
    @arguments('name')
    def run(I):
        I.validate_inputs
        I.persist_result

    def validate_inputs(self, ctx):
        return Success() if isinstance(ctx.name, str) and len(ctx.name) < 50 else Failure()

    def persist_result(self, ctx):
        ctx.result = self.repo.create_ingredient(ctx.name)
        return Result(ctx.result)


create_ingredient = CreateIngredient()
create_ingredient.repo = CatalogRepository()