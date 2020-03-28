from django.shortcuts import render
from rest_framework import generics,filters
from . import models, serializer


# Create your views here.
class ProductGenericView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    filter_backends = (filters.OrderingFilter,filters.SearchFilter)
    serializer_class = serializer.ProductSerializer
    filter_fields = ('name','quantity')
    search_fields = ('name','quantity')
    permission_classes = []

class ProductRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer
    permission_classes = []