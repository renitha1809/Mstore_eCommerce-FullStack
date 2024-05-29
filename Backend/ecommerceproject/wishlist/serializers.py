from rest_framework import serializers
from . models import Wishlist
from product.serializers import ProductDetailSerializer

class WishlistSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    product = serializers.CharField(read_only=True)
    
    class Meta:
        model=Wishlist
        fields=[
            "id",
            "user",
            "product",
            "quantity",
            "created_date",
            
        ]

class WishlistListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    product = ProductDetailSerializer()
    
    class Meta:
        model=Wishlist
        fields=[
            "id",
            "user",
            "product",
            "quantity",
            "created_date", 
        ]
    