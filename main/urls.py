
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from project.sitemaps import ProjectSitemap
from service.sitemaps import ServiceSitemap
from shop.sitemaps import ProductCategorySitemap, ProductBrandSitemap, ProductSitemap
from users.sitemaps import TeamSitemap

sitemaps = {
    'posts': PostSitemap,
    'services': ServiceSitemap,
    'products_by_category': ProductCategorySitemap,
    'products_by_brand': ProductBrandSitemap,
    'products': ProductSitemap,
    'projects': ProjectSitemap,
    'team': TeamSitemap,
}

urlpatterns = [
    path('', include('core.urls')),
    path('v-s/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('blogs/', include('blog.urls')),
    path('projects/', include('project.urls')),
    path('services/', include('service.urls')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('shop/', include('shop.urls')),
    path('users/', include('users.urls')),
    path('newsletter/', include('subscribe.urls')),
    path('ai/', include('ai.urls')),
    path('api/', include('api.urls')),
    path('gwd/', include('assignments.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitempas.views.sitemap'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'VSTech Admin'
admin.site.site_title = 'VSTech Admin'
