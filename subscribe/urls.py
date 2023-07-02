from . import views
from django.urls import path

app_name = 'subscribe'
urlpatterns = [
    path('', views.index, name='index'),
    path('subscribe/', views.new_subscriber, name='new'),
    path('send-email/', views.send_email_to_subscribers, name='send_email'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('templates/', views.view_templates, name='templates'),
    path('templates/default/', views.default, name='templates_default'),
    path('templates/blogs/', views.blogs, name='templates_blogs'),
    path('templates/products/', views.product, name='templates_products'),
]