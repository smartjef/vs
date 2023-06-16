from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='list'),
    path('brands/<slug:brand_slug>/', views.index, name='list_by_brand'),
    path('categories/<slug:category_slug>/', views.index, name='list_by_category'),
    path('cart/', views.cart_detail, name='cart'),
    path('<slug:slug>/', views.product_details, name='detail'),
    path('<slug:slug>/leave-review/', views.leave_review, name='add_review'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]
