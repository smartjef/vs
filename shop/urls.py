from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='list'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('<slug:slug>/', views.product_details, name='product_details'),
]
