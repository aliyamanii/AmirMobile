from rest_framework import viewsets, permissions, status, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.serializers import *


from django.db.models import OuterRef, Exists

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.filter(Exists(OrderDetail.objects.filter(order=OuterRef('id'))),)

class OrderDetailViewSet(viewsets.ModelViewSet):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetail.objects.all()

    def perform_create(self, serializer):
        try:
            object = self.get_queryset().get(order=serializer.validated_data['order']['id'], product=serializer.validated_data['product']['id'])
        except Exception as e:
            return super().perform_create(serializer)
        object.quantity += serializer.validated_data['quantity']
        object.total_cost += object.quantity * serializer.validated_data['product']['id'].price

        object.save()