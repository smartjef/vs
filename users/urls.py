from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('team/', views.team, name='team'),
    path('team/<slug:slug>/', views.team_details, name='team_details')
]
