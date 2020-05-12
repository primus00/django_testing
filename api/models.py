from django.db import models

# Create your models here.

class User(models.Model):
  name = models.CharField(max_length=100)
  description= models.TextField(max_length=5000)
  traits = models.CharField(max_length=100)

  def __str__(self):
    return self.name

"""
    @todo Add models for login
    @body There is a requirement of destroy action <br> ![img](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.M9AsZ7Sm6Qq-LXpY92Tt2AHaEK%26pid%3DApi&f=1) 
"""

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