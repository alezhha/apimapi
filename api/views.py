from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from .models import *
from .serializers import *
from django.contrib.auth import authenticate, login
from rest_framework.parsers import JSONParser

# Create your views here.

def meals(request):
  if request.method == 'GET':
    meals = Meal.objects.all()
    serializer = MealSerializer(meals, many = True)
    return JsonResponse(serializer.data, safe = False)

def meals_by_cat(request, category):
  if request.method == 'GET':
    try:
      category = Categories.objects.get(name = category)
      meals = Meal.objects.filter(category = category)
      serializer = MealSerializer(meals, many = True)
      return JsonResponse(serializer.data, safe = False)
    except Categories.DoesNotExist:
      return JsonResponse({'message':'No such Category'})

def meal_detail(request, id):
  if request.method == 'GET':
    try:
      meals = Meal.objects.filter(id = id)
      serializer = MealSerializer(meals, many = True)
      return JsonResponse(serializer.data, safe = False)
    except Meal.DoesNotExist:
      return JsonResponse({'message':'No such Meal'})

def reviews(request, meal):
  if request.method == 'GET':
    try:
      meal = Meal.objects.get(name = meal)
      reviews = Reviews.objects.filter(meal = meal)
      serializer = ReviewSerializer(reviews, many=True)
      return JsonResponse(serializer.data, safe = False)
    except Meal.DoesNotExist:
      return JsonResponse({'message':'No such Meal'})
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = ReviewSerializer(data = data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status = 201)
    return JsonResponse(serializer.errors, status = 400)

def delete_review(request, meal, id):
  if request.method == 'DELETE':
    try:
      meal = Meal.objects.get(name = meal)
      reviews = Reviews.objects.filter(meal = meal, id = id)
      reviews.delete()
      return redirect('/')
    except Reviews.DoesNotExist:
      return redirect('/')

def user(request):
  if request.method == 'GET':
    return JsonResponse({'users':list(User.objects.values())})
  elif request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return JsonResponse({'message':'Success!'})
    else:
      return JsonResponse({'message':'Invalid User!'})

def delete_user(request, id):
  if request.method == 'DELETE':
    try:
      user1 = User.objects.get(id = id)
      user1.delete()
      return redirect('/api/user')
    except User.DoesNotExist:
      return redirect('/api/user')