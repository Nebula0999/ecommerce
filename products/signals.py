from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ValidationError
from .models import OrderItem

@receiver(post_save, sender=OrderItem) # Signal to reduce stock when an order is placed
def reduce_stock(sender, instance, created, **kwargs): # Function to reduce stock
    if created:  # Check if the instance was created
        product = instance.product
        if product.stock_Quantity >= instance.quantity:
            product.stock_Quantity -= instance.quantity
            product.save() # Save the product
        else: 
            # Raise ValidationError with a custom message
            raise ValidationError(
                f"Not enough stock for product '{product.name}'. Available stock: {product.stock_Quantity}, requested: {instance.quantity}."
            ) # Return a message if there is not enough stock