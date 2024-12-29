from rest_framework.routers import DefaultRouter
from django.urls import path
from products.views import ProductViewSet, CategoryViewSet, UserViewSet, OrderViewSet, ProductListView, OrderItemView, ProductReviewSet
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter() # Create a router

router.register('view-products', ProductListView, basename='view-products') # Register the view
router.register('products', ProductViewSet)
router.register('users', UserViewSet)
router.register('orders', OrderViewSet)
router.register('category', CategoryViewSet)
router.register('order-item', OrderItemView)
router.register('reviews', ProductReviewSet)
#router.register('search', ProductFilter, basename='product_filter')

urlpatterns = [path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),] + router.urls # Add the token URL to the list of URLs
