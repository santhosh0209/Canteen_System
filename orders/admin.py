from django.contrib import admin

from .models import Food, OrderItem, Order


admin.site.register(Food)
admin.site.register(OrderItem)
admin.site.register(Order)
