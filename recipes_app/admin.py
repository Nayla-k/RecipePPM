from django.contrib import admin
from . import models




admin.site.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "meal_type",
        "instructions",
        "ingredients",
    )
    list_filter = ("meal_type",)

