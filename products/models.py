from django.db import models
from django.core.exceptions import ValidationError
from users.models import User

#def validate_value(value):
    #if value is not True:
        #raise ValidationError ("Field is required")
class Category(models.Model): # Category model
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self): # String representation of the model
        return self.name
class Products(models.Model): # Product model
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=255)
    price = models.IntegerField(blank=False)
    category = models.ForeignKey(Category, related_name='type', on_delete=models.CASCADE)
    stock_Quantity = models.PositiveIntegerField(blank=False)
    image_URL = models.URLField()
    created_Date = models.DateTimeField(auto_now=True)

    def __str__(self):  # String representation of the model
        return self.name
    
class Order(models.Model): # Order model
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, default="pending")

class OrderItem(models.Model): # OrderItem model
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="item")
    quantity = models.PositiveIntegerField()

    def __str__(self): # String representation of the model
            return f"{self.quantity} of {self.product.name}"
    
class ProductReview(models.Model): # ProductReview model
     name = models.CharField(max_length=50, blank=False, null=True)
     product = models.ForeignKey(Products, on_delete=models.CASCADE)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     comment = models.TextField(max_length=200, blank=True)
     rating =  rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 11)])
     created_at = models.DateTimeField(auto_now=True)

     def __str__(self): # String representation of the model
        return f"Review for {self.product.name} by {self.user.username}"



# Create your models here.
