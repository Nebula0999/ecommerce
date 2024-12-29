from django.shortcuts import render
from requests import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from api.serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import filters, status
from django_filters.rest_framework import DjangoFilterBackend
from users.models import User
from api.serializers import ProductSerializer, CategorySerializer, UserSerializer, OrderSerializer, OrderItemSerializer, ProductReviewSerializer
from products.models import Products, Order, Category, OrderItem, ProductReview
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django_filters import FilterSet

class CustomPagination(PageNumberPagination):
    page_size = 50  # Custom pagination to display upto 50 products per page

def ProductsFilter(FilterSet):
    class Meta:
        model = Products
        fields = ['id', 'name']  # filter products by id and name

class ProductListView(ReadOnlyModelViewSet): # read only view for products
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination # pagination for the products

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['products', 'category']

    def get(self, request, *args, **kwargs):
       # Get the filtered queryset
       queryset = self.filter_queryset(self.get_queryset())

       page = self.paginate_queryset(queryset) # paginate the queryset
       if page is not None:
           serializer = self.get_serializer(page, many=True)
           return self.get_paginated_response(serializer.data)

class ProductViewSet(ModelViewSet): # view for products that allows CRUD operations
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination # pagination for the products
    permission_classes = [IsAuthenticated] # only authenticated users can perform CRUD operations

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content) # return response if request is permitted

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['products', 'category']

    def get(self, request, *args, **kwargs):
       # Get the filtered queryset
       queryset = self.filter_queryset(self.get_queryset())

       page = self.paginate_queryset(queryset)
       if page is not None: 
           serializer = self.get_serializer(page, many=True)
           return self.get_paginated_response(serializer.data) # return paginated response

class CategoryViewSet(ModelViewSet): # view for categories that allows CRUD operations
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class OrderViewSet(ModelViewSet): # view for orders that allows CRUD operations
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated] # only authenticated users can perform CRUD operations

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content) # return response if request is permitted

    
class UserViewSet(ReadOnlyModelViewSet): # read only view for users
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated] # only authenticated users can view users

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content) # return response if request is permitted
    
class OrderItemView(ModelViewSet): # view for order items that allows CRUD operations
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated] # only authenticated users can perform CRUD operations

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content) # return response if request is permitted

class ProductReviewSet(ModelViewSet): # view for product reviews that allows CRUD operations
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [IsAuthenticated] # only authenticated users can perform CRUD operations

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content) # return response if request is permitted
        

# Create your views here.