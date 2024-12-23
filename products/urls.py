from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductView.as_view(), name='products'),
    path('location/', views.LocationView.as_view(), name='location'),
]