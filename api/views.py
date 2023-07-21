from django.shortcuts import render
from service.models import Service
from core.models import About, FAQ, Partner, Testimony
from blog.models import Post
from shop.models import Product
from project.models import Project
from rest_framework import generics
from .serializers import ServiceSerializer, AboutSerializer, FAQSerializer, PartnerSerializer, TestimonySerializer, PostSerializer, ProjectSerializer, ProductSerializer
# Create your views here.
class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class AboutListView(generics.ListAPIView):
    queryset = About.objects.filter(is_active=True)
    serializer_class = AboutSerializer

class AboutDetailView(generics.RetrieveAPIView):
    queryset = About.objects.filter(is_active=True)
    serializer_class = AboutSerializer

class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.filter(is_active=True)
    serializer_class = FAQSerializer

class FAQDetailView(generics.RetrieveAPIView):
    queryset = FAQ.objects.filter(is_active=True)
    serializer_class = FAQSerializer

class PartnerListView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class PartnerDetailView(generics.RetrieveAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class TestimonyListView(generics.ListAPIView):
    queryset = Testimony.objects.filter(is_active=True)
    serializer_class = TestimonySerializer

class TestimonyDetailView(generics.RetrieveAPIView):
    queryset = Testimony.objects.filter(is_active=True)
    serializer_class = TestimonySerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer

class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_approved=True)
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_approved=True)
    serializer_class = ProductSerializer