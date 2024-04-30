from django.urls import path
from .views import index, add_recipe, show_recipe

urlpatterns = [
    path("", index),
    path("add/", add_recipe),
    path("recipe/<str:id>", show_recipe),
    
]
