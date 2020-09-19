from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_favorites, name="my_favorites"),
    path('add/<item_id>/', views.add_to_favorites, name="add_to_favorites"),
    path('delete/<item_id>/', views.remove_from_favorites,
         name="remove_from_favorites"),
]
