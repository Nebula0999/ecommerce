from django.contrib import admin
from .models import Products, Category, Order, OrderItem, ProductReview
from django.utils.html import format_html

class OrderAdmin(admin.ModelAdmin): # Admin class for Order
    pass

class OrderItemAdmin(admin.ModelAdmin): # Admin class for OrderItem
    list_display = ('product', 'quantity', 'order')

    def save_model(self, request, obj, form, change):
        product = obj.product
        if product.stock_Quantity < obj.quantity:
            # Display a user-friendly error message in the admin interface
            self.message_user(
                request,
                format_html(
                    f"Error: Not enough stock for product '{product.name}'. Available stock: {product.stock_Quantity}, requested: {obj.quantity}."
                ),
                level="error",
            )
        else:
            # Reduce stock if valid
            product.stock_Quantity -= obj.quantity
            product.save()
            super().save_model(request, obj, form, change)


class CategoryAdmin(admin.ModelAdmin): # Admin class for Category
    pass

class ProductReviewAdmin(admin.ModelAdmin): # Admin class for ProductReview
    pass

admin.site.register(Products) # Register Products, Category, Order, OrderItem, and ProductReview models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
# Register your models here.
