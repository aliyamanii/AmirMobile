from rest_framework.routers import DefaultRouter

from api.views import BrandViewSet, OrderViewSet, OrderDetailViewSet, ProductViewSet

router = DefaultRouter()
router.register('brands', BrandViewSet, basename='brand')
router.register('products', ProductViewSet, basename='product')
router.register('orders', OrderViewSet, basename='order')
router.register('order_details', OrderDetailViewSet, basename='order_detail')

urlpatterns = router.urls