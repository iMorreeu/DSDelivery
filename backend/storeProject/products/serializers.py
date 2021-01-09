from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    formatted_uri = serializers.CharField(required=False)

    class Meta:
        model = Product
        fields = "__all__"
