from django.db import models

# Create your models here.
"""
    @todo Add models api.models
    @body There is a requirement of destroy action \\
          ### is a requirement of destroy action \\ 
          There is a requirement of destroy action \\
          * is a requirement of destroy action \\
          * is a requirement of destroy action \\ 
          - [ ] is a requirement of destroy action \\
"""

class User(models.Model):
  name = models.CharField(max_length=100)
  description= models.TextField(max_length=5000)
  traits = models.CharField(max_length=100)

  def __str__(self):
    return self.name


class User2(models.Model):
  name = models.CharField(max_length=100)
  description= models.TextField(max_length=5000)
  traits = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class User3(models.Model):
  name = models.CharField(max_length=100)
  description= models.TextField(max_length=5000)
  traits = models.CharField(max_length=100)

  def __str__(self):
    return self.name