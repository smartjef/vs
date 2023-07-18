"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
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
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitempas.views.sitemap'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'VSTech Admin'
admin.site.site_title = 'VSTech Admin'
