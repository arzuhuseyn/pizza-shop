from stories import story, arguments, Success, Result, Failure

from catalog.repository import CatalogRepository


class UpdateIngredient:
    @story
    @arguments('pk', 'name')
    def run(I):
        I.validate_inputs
        I.persist_result

    def validate_inputs(self, ctx):
        if bool(self.repo.get_ingredient(ctx.pk)) and isinstance(ctx.name, str):
            return Success()
        return Failure()

    def persist_result(self, ctx):
        ctx.result = self.repo.update_ingredient(ctx.pk, ctx.params)
        return Result(ctx.result)


update_ingredient = UpdateIngredient()
update_ingredient.repo = CatalogRepository()