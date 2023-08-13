from . import views
from django.urls import path

app_name = 'edu'

urlpatterns =[
    path('', views.index, name='index'),
    path('schools/<slug:school_slug>/', views.index, name='notes_by_school'),
    path('units/<slug:unit_slug>/', views.index, name='notes_by_unit'),
    path('resources/', views.resources, name='resources'),
]