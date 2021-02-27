from django.contrib import admin
from .models import *

# Register your models here.


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ('name', 'price')

    class Meta:
        model = Product


class ProductImageAdmin(admin.ModelAdmin):
    pass


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')


admin.site.site_header = "myShop Dashboard"
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
