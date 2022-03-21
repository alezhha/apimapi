from rest_framework import serializers
from .models import *

class MealSerializer(serializers.ModelSerializer):
  class Meta:
    model = Meal
    fields = ["id", "name", "description", 'image', 'price', 'ingredients', 'size', 'category']

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Categories
    fields = ["id", 'name', 'description']

class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reviews
    fields = ["id", 'user', 'rate', 'text', 'date', 'meal']