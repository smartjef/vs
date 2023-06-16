from django.contrib import admin
from .models import ProductCategory, Product, Brand, ProductImage, Review
# Register your models here.

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    list_filter = ['created_at', 'updated_at']
    search_fields =['title', 'slug',]
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    list_filter = ['created_at', 'updated_at']
    search_fields =['title', 'slug',]
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'

class ProductImageInline(admin.TabularInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'current_price', 'discount', 'is_approved', 'in_stock', 'created_at', 'updated_at']
    list_filter = ['category', 'created_at', 'updated_at']
    search_fields =['title', 'current_price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    inlines = [ProductImageInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['message', 'product', 'user', 'rating', 'is_active', 'created_at']
    list_filter = ['created_at', 'rating', 'is_active']
    search_fields = ['author_username', 'message',]
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
