class OrderItemFactory:
    def __init__(self, item_id, size, count, ingredients):
        self.item_id = item_id
        self.size = size 
        self.count = count
        self.ingredients = ingredients

    def get_object(self):
        return self.repo.get_pizza(self.item_id)
    
    def build_ingredients(self):
        return [ingredient.name for ingredient in self.repo.get_ingredients_by_id(self.ingredients)]

    def build(self, **kwargs):
        obj = self.get_object()
        img = obj.image.url if obj.image else None
        return {
            'id' : obj.id,
            'name': obj.name,
            'image': img,
            'size': self.size,
            'count': self.count,
            'ingredients': self.build_ingredients(),
        }