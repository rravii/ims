from django.shortcuts import render
from rest_framework import generics
from . import models, serializer


# Create your views here.
class ProductGenericView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer
    permission_classes = []

class ProductRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer
    permission_classes = []