from . import views
from django.urls import path

app_name = 'subscribe'
urlpatterns = [
    path('new/', views.new_subscriber, name='new'),
]