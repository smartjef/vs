from django.contrib.sitemaps import Sitemap

from .models import Product, ProductCategory, Brand


class ProductCategorySitemap(Sitemap):
    changefreq = 'always'
    priority = 0.9

    def items(self):
        return ProductCategory.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return obj.get_absolute_url()
    
class ProductBrandSitemap(Sitemap):
    changefreq = 'always'
    priority = 0.9

    def items(self):
        return Brand.objects.a()

    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return obj.get_absolute_url()
    
class ProductSitemap(Sitemap):
    changefreq = 'always'
    priority = 0.9

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return obj.get_absolute_url()