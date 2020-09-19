from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_request, name="contact_request"),
    path('quotation/<item_id>/', views.quotation_request, name="quotation_request"),
]
