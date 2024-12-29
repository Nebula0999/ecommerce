from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ValidationError
from .models import OrderItem

@receiver(post_save, sender=OrderItem)
def reduce_stock(sender, instance, created, **kwargs):
    if created: 
        product = instance.product
        if product.stock_Quantity >= instance.quantity:
            product.stock_Quantity -= instance.quantity
            product.save()
        else:
            # Raise ValidationError with a custom message
            raise ValidationError(
                f"Not enough stock for product '{product.name}'. Available stock: {product.stock_Quantity}, requested: {instance.quantity}."
            )