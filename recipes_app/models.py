from django.db import models
from django.contrib.auth.models import User

MEAL_TYPES = (("breakfast", "Breakfast"), ("lunch", "Lunch"), ("dinner", "Dinner"),("dessert","Dessert"))

CUISINE_TYPES = (
    ("italian","Italian"),
    ("african", "African"),
    ("american", "American"),
    ("caribbean", "Caribbean"),
    ("asian", "Asian"),
    ("middle_eastern", "Middle Eastern"),
    ("chinese", "Chinese"),
    ("indian", "Indian"),
    ("pakistani", "Pakistani"),
    ("indonesian", "Indonesian"),
    ("european", "European"),
    ("oceanic", "Oceanic"),
)


class Recipe(models.Model):
    """
    A model to create and manage recipes
    """

    author = models.ForeignKey(
        User, related_name="recipe_owner", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    instructions = models.CharField(max_length=10000, null=False, blank=False)
    ingredients = models.CharField(max_length=10000, null=False, blank=False)
    meal_type = models.CharField(max_length=50, choices=MEAL_TYPES, default="breakfast")
    cuisine_types = models.CharField(
        max_length=50, choices=CUISINE_TYPES, default="italian"
    )
    posted_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return str(self.title)
    
class AddRecipe(models.Model) :
    """
        model to add recipe
    """
    model: Recipe
    success_url = '/recipes/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)