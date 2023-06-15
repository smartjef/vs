from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='list'),
    path('brands/<slug:brand_slug>/', views.index, name='list_by_brand'),
    path('categories/<slug:category_slug>/', views.index, name='list_by_category'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('<slug:slug>/', views.product_details, name='detail'),
]
