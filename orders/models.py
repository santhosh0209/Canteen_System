from django.db import models
from datetime import datetime

from django.conf import settings
from django.contrib import auth
from django.urls import reverse


class User(auth.models.User, auth.models.PermissionsMixin, models.Model):


    def __str__(self):
        return self.username

class Food(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
    
    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            'pk': self.pk
        })

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            'pk': self.pk
        })
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Food, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_final_price(self):
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    class Meta:
        verbose_name = " Ordered Detail"
        verbose_name_plural = " Ordered Details"

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total


    