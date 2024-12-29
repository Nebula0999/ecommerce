from django.shortcuts import render
from requests import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
    page_size = 50  

class PermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated

def ProductsFilter(FilterSet):
    class Meta:
        model = Products
        fields = ['id', 'name']  

class ProductListView(ListView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['products', 'category']

    def get(self, request, *args, **kwargs):
       # Get the filtered queryset
       queryset = self.filter_queryset(self.get_queryset())

       page = self.paginate_queryset(queryset)
       if page is not None:
           serializer = self.get_serializer(page, many=True)
           return self.get_paginated_response(serializer.data)

class ProductViewSet(DetailView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['products', 'category']

    def get(self, request, *args, **kwargs):
       # Get the filtered queryset
       queryset = self.filter_queryset(self.get_queryset())

       page = self.paginate_queryset(queryset)
       if page is not None:
           serializer = self.get_serializer(page, many=True)
           return self.get_paginated_response(serializer.data)
       
class ProductCreateView(PermissionMixin, CreateAPIView):
    model = Products
    fields = '__all__'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
class ProductUpdateView(PermissionMixin, UpdateView):
    model = Products
    fields = '__all__'
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

   
class ProductDeleteView(PermissionMixin, DeleteView):
    model = Products
    success_url = '/products/'

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.creator

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)

    
class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
    
class OrderItemView(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)

class ProductReviewSet(ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
        

# Create your views here.
