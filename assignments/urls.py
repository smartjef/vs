from django.urls import path
from . import views

app_name = 'assignment'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard')
]