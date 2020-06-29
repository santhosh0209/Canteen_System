from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView


from .views import (
    HomeView, signup_view,
    CheckoutView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    AddCouponView,
    remove_single_item_from_cart,
)

urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('signup/', signup_view, name = "signup"),
    path('login/', LoginView.as_view(template_name = 'login.html'), name = "login"),
    path('logout/', LogoutView.as_view(), name = "logout"),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('add-to-cart/<pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<pk>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<pk>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),


]
