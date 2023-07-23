from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('about', views.AboutViewSet, basename='about')
router.register('services', views.ServiceViewSet, basename='service')
router.register('services/(?P<service_pk>\d+)/faqs', views.ServiceFAQViewSet, basename='service-faq')
router.register('posts', views.PostViewSet, basename='post')
router.register('posts/(?P<post_pk>\d+)/comments', views.PostCommentViewSet, basename='post-comment')
router.register('comments/(?P<comment_pk>\d+)/replies', views.CommentReplyViewSet, basename='comment-reply')
router.register('team', views.TeamViewSet, basename='team')
router.register('tags', views.TagViewSet, basename='tag')
router.register('tags/(?P<tag_pk>\d+)/posts', views.TagPostViewSet, basename='tag-post')
router.register('categories', views.CategoryViewSet, basename='category')
router.register('categories/(?P<category_pk>\d+)/posts', views.CategoryPostViewSet, basename='category-post')
router.register('projects', views.ProjectViewSet, basename='project')
router.register('testimonies', views.TestimonyViewSet, basename='testimony')
router.register('faqs', views.FAQViewSet, basename='faq')
router.register('partners', views.PartnerViewSet, basename='partner')
router.register('product-categories', views.ProductCategoryViewSet, basename='product-category')
router.register('product-categories/(?P<category_pk>\d+)/products', views.CategoryProductViewSet, basename='category-product')
router.register('brands', views.BrandViewSet, basename='brands')
router.register('brands/(?P<brand_pk>\d+)/products', views.BrandProductsViewSet, basename='brand-product')
router.register('products', views.ProductViewSet, basename='products')
router.register('products/(?P<product_pk>\d+)/reviews', views.ProductReviewViewSet, basename='product-review')
router.register('products/(?P<product_pk>\d+)/images', views.ProductImageViewSet, basename='product-image')
router.register('contacts', views.ContactCreateViewSet, basename='contact')
router.register('descriptions', views.ImageDescritionViewSet, basename='ai-image-description')
router.register('descriptions/(?P<description_pk>\d+)/images', views.GeneratedImagesViewSet, basename='ai-generated-image')
router.register('subscribe', views.SubscriberViewSet, basename='subscribe')

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]