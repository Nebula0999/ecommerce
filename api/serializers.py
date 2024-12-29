from rest_framework.serializers import ModelSerializer, ValidationError
from products.models import Products, Category, Order, OrderItem, ProductReview
from users.models import User

class ProductSerializer(ModelSerializer): # Serializer class for products
    class Meta:
        model = Products
        fields = '__all__'
class CategorySerializer(ModelSerializer): # Serializer class for categories
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(ModelSerializer): # Serializer class for users
    class Meta:
        model = User
        fields = '__all__'

class OrderSerializer(ModelSerializer): # Serializer class for orders
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(ModelSerializer): # Serializer class for order items
    class Meta:
        model = OrderItem
        fields = "__all__"

    def validate(self, data): # Validate the order item
        product = data['product']
        if product.stock < data['quantity']:
            raise ValidationError(f"Not enough stock for product {product.name}.")
        return data # return the data
    
class ProductReviewSerializer(ModelSerializer): # Serializer class for product reviews
     class Meta:
        model = ProductReview
        fields = '__all__'