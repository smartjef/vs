from rest_framework import serializers
from service.models import Service, ServiceFAQ
from core.models import About, Partner, FAQ, Testimony, Tag, Category
from django.contrib.auth.models import User
from users.models import Profile
from blog.models import Post, Comment, Reply
from project.models import Project
from shop.models import ProductCategory, Brand, Product, ProductImage, Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug'] 

class ProjectSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    class Meta:
        model = Project
        fields = ['title', 'slug', 'category', 'front_image', 'cover_image', 'description', 'website', 'client', 'date_completed', 'is_active', 'created_at'] 

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title', 'slug'] 

class ServiceFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceFAQ
        fields = ['id', 'question', 'answer', 'is_active', 'created_at'] 

class ServiceSerializer(serializers.ModelSerializer):
    faqs = ServiceFAQSerializer(many=True, read_only=True)
    class Meta:
        model = Service
        fields = ['title', 'description', 'front_image', 'cover_image', 'faqs']

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['title', 'phone_number', 'email', 'twitter', 'facebook', 'linkedin', 'youtube', 'github', 'address', 'created_at']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image',]

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False, read_only=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'profile']

class TestimonySerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Testimony
        fields = ['position', 'message', 'rating', 'is_active', 'created_at', 'author']

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['title', 'website', 'logo', 'created_at']

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['question', 'answer', 'is_active', 'created_at']

class ReplySerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Reply
        fields = ['author', 'message', 'is_approved', 'created_at']  

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False, read_only=True)
    replies = ReplySerializer(many=True, read_only=True)
    class Meta:
        model = Comment
        fields = ['author', 'message', 'is_approved', 'created_at', 'replies']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['title', 'slug', 'category', 'author', 'body', 'tags', 'front_image', 'cover_image', 'views', 'likes', 'dislikes', 'created_at', 'comments']
   

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['title', 'slug']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['title', 'slug']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Review
        fields = ['user', 'message', 'rating', 'is_active', 'created_at']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(many=False, read_only=True)
    brand = BrandSerializer(many=False, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['title', 'category', 'brand', 'slug', 'image', 'description', 'current_price', 'discount', 'in_stock', 'is_approved', 'created_at', 'images', 'reviews']
