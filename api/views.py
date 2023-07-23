from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from service.models import Service, ServiceFAQ
from core.models import About, FAQ, Partner, Testimony, Tag, Category, Contact
from users.models import Team
from blog.models import Post, Comment, Reply
from shop.models import Product, ProductCategory, Brand, Review, ProductImage
from project.models import Project
from ai.models import GeneratedImage, ImageDescription
from subscribe.models import Subscriber
from .serializers import ServiceSerializer, AboutSerializer, FAQSerializer, PartnerSerializer, TestimonySerializer, PostSerializer, ProjectSerializer, ProductSerializer, ServiceFAQSerializer, TeamSerializer, CommentSerializer, ReplySerializer, TagSerializer, CategorySerializer, ProductCategorySerializer, BrandSerializer, ReviewSerializer, ProductImageSerializer, ContactSerializer, ImageDescriptionSerializer, GeneratedImagesSerializer, SubscriberSerializer
# Create your views here.

class IsObjOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
    
class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceFAQViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ServiceFAQSerializer

    def get_queryset(self):
        service_pk = self.kwargs.get('service_pk')
        service = get_object_or_404(Service, pk=service_pk)
        queryset = ServiceFAQ.objects.filter(service=service)
        return queryset

class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.filter(is_active=True)
    serializer_class = TeamSerializer

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer

class PostCommentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_pk = self.kwargs.get('post_pk')
        post = get_object_or_404(Post, pk=post_pk, is_published=True)
        queryset = Comment.objects.filter(post=post, is_approved=True)
        return queryset
    
class CommentReplyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ReplySerializer

    def get_queryset(self):
        comment_pk = self.kwargs.get('comment_pk')
        comment = get_object_or_404(Comment, pk=comment_pk, is_approved=True)
        queryset = Reply.objects.filter(comment=comment, is_approved=True)
        return queryset
    
class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.filter(is_active=True)
    serializer_class = AboutSerializer

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagPostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        tag_pk = self.kwargs.get('tag_pk')
        tag = get_object_or_404(Tag, pk=tag_pk)
        queryset = Post.objects.filter(tags=tag, is_published=True)
        return queryset
    
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryPostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        category_pk = self.kwargs.get('category_pk')
        category = get_object_or_404(Category, pk=category_pk)
        queryset = Post.objects.filter(category=category, is_published=True)
        return queryset

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer

class TestimonyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimony.objects.filter(is_active=True)
    serializer_class = TestimonySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."},
                            status=status.HTTP_401_UNAUTHORIZED)

        serializer = TestimonySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FAQViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FAQ.objects.filter(is_active=True)
    serializer_class = FAQSerializer

class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(is_approved=True)
    serializer_class = ProductSerializer

class ProductCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class CategoryProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_pk = self.kwargs.get('category_pk')
        category = get_object_or_404(ProductCategory, pk=category_pk)
        queryset = Product.objects.filter(category=category, is_approved=True)
        return queryset

class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandProductsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        brand_pk = self.kwargs.get('brand_pk')
        brand = get_object_or_404(Brand, pk=brand_pk)
        queryset = Product.objects.filter(brand=brand, is_approved=True)
        return queryset

class ProductReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsObjOwner]

    def get_queryset(self):
        product_pk = self.kwargs.get('product_pk')
        product = get_object_or_404(Product, pk=product_pk, is_approved=True)
        queryset = Review.objects.filter(product=product, is_active=True)
        return queryset

    def perform_create(self, serializer):
        product_pk = self.kwargs.get('product_pk')
        product = get_object_or_404(Product, pk=product_pk, is_approved=True)
        serializer.save(product=product, user=self.request.user)

class ProductImageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        product_pk = self.kwargs.get('product_pk')
        product = get_object_or_404(Product, pk=product_pk, is_approved=True)
        queryset = ProductImage.objects.filter(product=product)
        return queryset
    

class ContactCreateViewSet(viewsets.ViewSet):
    permission_classes = []

    def get_queryset(self):
        return Contact.objects.none()

    def create(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ImageDescritionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ImageDescriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = ImageDescription.objects.filter(user=user)
        return queryset


class GeneratedImagesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GeneratedImagesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        description_pk = self.kwargs.get('description_pk')
        queryset = GeneratedImage.objects.filter(description__user=user, description_id=description_pk, is_active=True)
        return queryset
    
class SubscriberViewSet(viewsets.ViewSet):
    serializer_class = SubscriberSerializer

    def get_queryset(self):
        return Subscriber.objects.none()  

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')

            if Subscriber.objects.filter(email=email).exists():
                return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

