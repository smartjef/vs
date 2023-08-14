from django.contrib.sitemaps import Sitemap

from .models import School, UnitName, Note


class SchoolSitemap(Sitemap):
    changefreq = 'always'
    priority = 0.9

    def items(self):
        return School.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return obj.get_absolute_url()
    
class UnitNameSitemap(Sitemap):
    changefreq = 'always'
    priority = 0.9

    def items(self):
        return UnitName.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return obj.get_absolute_url()
    
class NoteSitemap(Sitemap):
    changefreq = 'always'
    priority = 0.9

    def items(self):
        return Note.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return obj.file.url