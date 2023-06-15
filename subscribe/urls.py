from . import views
from django.urls import path

app_name = 'subscribe'
urlpatterns = [
    path('', views.index, name='index'),
    path('subscribe/', views.new_subscriber, name='new'),
]