from django.urls import path
from .views import *

urlpatterns = [
    path('meals/', meals),
    path('meals_category/<str:category>', meals_by_cat),
    path('meal_detail/<int:id>', meal_detail),
    path('reviews/<str:meal>', reviews),
    # path('delete_review/<str:meal>/<int:id>', delete_meal),
    path('user/', user, name='usersPage'),
    path('delete_user/<int:id>', delete_user),
]
