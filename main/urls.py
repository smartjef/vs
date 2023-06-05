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

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('blogs/', include('blog.urls')),
    path('projects/', include('project.urls')),
    path('services/', include('service.urls')),
    path('shop/', include('shop.urls')),
    path('users/', include('users.urls')),
    path('subscribe/', include('subscribe.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'VSTech Admin'
admin.site.site_title = 'VSTech Admin'
