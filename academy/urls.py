from . import views
from django.urls import path

app_name = 'edu'

urlpatterns =[
    path('', views.index, name='index'),
    path('resources/', views.resources, name='resources'),
]