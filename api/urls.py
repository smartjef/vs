from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'api'
urlpatterns = [
    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('services/<pk>/',views.ServiceDetailView.as_view(),name='service_detail'),
    path('about/', views.AboutListView.as_view(), name='about_list'),
    path('about/<pk>/',views.AboutDetailView.as_view(),name='about_detail'),
    path('partners/', views.PartnerListView.as_view(), name='partner_list'),
    path('partners/<pk>/',views.PartnerDetailView.as_view(),name='partner_detail'),  
    path('faqs/', views.FAQListView.as_view(), name='faq_list'),
    path('faqs/<pk>/',views.FAQDetailView.as_view(),name='faq_detail'),
    path('testimonies/', views.TestimonyListView.as_view(), name='testimony_list'),
    path('testimonies/<pk>/',views.TestimonyDetailView.as_view(),name='testimony_detail'),  
    path('posts/', views.PostListView.as_view(), name='posts_list'),
    path('posts/<pk>/',views.PostDetailView.as_view(),name='posts_detail'),  
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('projects/<pk>/',views.ProjectDetailView.as_view(),name='project_detail'), 
    path('products/', views.ProductListView.as_view(), name='project_list'),
    path('products/<pk>/',views.ProductDetailView.as_view(),name='project_detail'), 
]