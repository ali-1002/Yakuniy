from django.db import models

class RecipeModel(models.Model):
    product = models.CharField(max_length=50)
    dickription = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.praduct}"
    
class FoodModel(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    recipes = models.ForeignKey(RecipeModel, on_delete=models.CASCADE, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "food"