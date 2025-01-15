
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from project.sitemaps import ProjectSitemap
from service.sitemaps import ServiceSitemap
from users.sitemaps import TeamSitemap
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

# API_TITLE = 'VSTech API'
# API_DESCRIPTION = 'VSTech Own API for creating and modifying applications/modules within the Company.'

# schema_view = get_schema_view(title=API_TITLE, description=API_DESCRIPTION)

sitemaps = {
    'posts': PostSitemap,
    'services': ServiceSitemap,
    'projects': ProjectSitemap,
    'team': TeamSitemap,
}

urlpatterns = [
    path('', include('core.urls')),
    path('v-s/', admin.site.urls),
    path('blogs/', include('blog.urls')),
    path('projects/', include('project.urls')),
    path('services/', include('service.urls')),
    path('users/', include('users.urls')),
    path('api/', include('api.urls')),
    # path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    # path('schema/', schema_view),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitempas.views.sitemap'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'VSTech Admin'
admin.site.site_title = 'VSTech Admin'
