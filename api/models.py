from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.


class Meal(models.Model):
  pizzaSize = [
      ('Small', 'Маленький'),
      ('Medium', 'Средний'),
      ('Large', 'Большой'),
  ]

  name = models.CharField(max_length=100)
  description = models.CharField(max_length=1000)
  image = models.ImageField(upload_to=None,)
  price = models.IntegerField(default=0)
  ingredients = models.JSONField(default=dict)
  size = models.CharField(choices=pizzaSize, max_length=100)
  category = models.ForeignKey('Categories', on_delete=models.CASCADE)

  def __str__(self):
    return self.name


class Categories(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=1000)

  def __str__(self):
    return self.name


class Reviews(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  rate = models.IntegerField(default=1, validators=[ MaxValueValidator(100), MinValueValidator(1) ])
  text = models.CharField(max_length=300)
  date = models.DateField(auto_now_add=True)
  meal = models.ForeignKey('Meal', on_delete=models.CASCADE)

  def __str__(self):
    return self.user.username
