from django.urls import path
from . import views
app_name = 'ai'

urlpatterns = [
    path('chat/', views.chat, name='chat'),
    path('desc-to-image/', views.desc_to_image, name='desc_to_image'),
    path('desc-to-image/<int:id>/delete/', views.delete_generated_image, name='delete_generated_image'),
]