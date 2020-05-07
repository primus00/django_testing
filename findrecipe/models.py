from django.db import models

# Create your models here.

class Ingredient(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Recipe(models.Model):
  name = models.CharField(max_length=200)
  description= models.TextField(max_length=5000)
  ingredient = models.ManyToManyField(Ingredient)

  def __str__(self):
    return self.name
