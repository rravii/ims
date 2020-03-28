from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
       name = serializers.CharField(required=True)
       quantity = serializers.IntegerField(required=True)