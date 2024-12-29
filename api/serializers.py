from rest_framework.serializers import ModelSerializer, ValidationError
from products.models import Products, Category, Order, OrderItem, ProductReview
from users.models import User

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

    def validate(self, data):
        product = data['product']
        if product.stock < data['quantity']:
            raise ValidationError(f"Not enough stock for product {product.name}.")
        return data
    
class ProductReviewSerializer(ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'