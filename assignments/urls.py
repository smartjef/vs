from django.urls import path
from . import views

app_name = 'gwd'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('referals/', views.referals, name='referals'),
    path('orders/', views.orders, name='orders'),
    path('earnings/', views.earnings, name='earnings'),
    path('withdrawals/', views.withdrawals, name='withdrawals'),
    path('place-an-order/', views.place_an_order, name='place_an_order'),
    path('<int:user_id>/get-code/', views.generate_code, name='get_code'),
]