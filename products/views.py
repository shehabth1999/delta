from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .serializers import ProductsSerializer, LocationSerializer
from .models import Product, Location

class ProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    filterset_fields = ('location',)
    search_fields = ('title',)

class LocationView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filterset_fields = ('location',)
    search_fields = ('location',)
