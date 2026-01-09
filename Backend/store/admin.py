from django.contrib import admin
from .models import Category, Order, Product, OrderItems, UserProfile

admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(Product)
admin.site.register(UserProfile)

