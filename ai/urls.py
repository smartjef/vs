from django.urls import path
from . import views
app_name = 'ai'

urlpatterns = [
    path('chat/', views.chat, name='chat'),
    path('desc-to-image/', views.desc_to_image, name='desc_to_image'),
    path('desc-to-image/<int:id>/delete/', views.delete_generated_image, name='delete_generated_image'),
    path('regenerate-image/<int:image_id>/', views.regenerate_image, name='regenerate_image'),
    path('get-ideas/', views.get_ideas, name='get_ideas'),
    path('make-payment/<str:payment_code>/', views.make_payment, name='make_payment'),
]