from rest_framework import serializers
from rest_framework.fields import HiddenField, BooleanField
from rest_framework.relations import SlugRelatedField

from api.models import *


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand_name', read_only=True)
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(write_only=True, source="order.id", queryset=Order.objects.all())

    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(write_only=True, source="product.id", queryset=Product.objects.all())

    class Meta:
        model = OrderDetail
        fields = '__all__'
        read_only_fields = ['total_cost']

    def create(self, validated_data):
        product = validated_data['product']['id']
        del validated_data['product']

        validated_data['product'] = product

        pid = validated_data['order']['id']
        del validated_data['order']

        validated_data['order'] = pid
        validated_data['total_cost'] = product.price * validated_data['quantity']
        
        return super().create(validated_data)