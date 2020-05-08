from django.contrib import admin
from .models import Recipe, Recipe2, Ingredient
# Register your models here.
admin.site.register(Recipe)
admin.site.register(Recipe2)
admin.site.register(Ingredient)