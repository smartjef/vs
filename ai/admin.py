from django.contrib import admin
from .models import GeneratedImage, Trial, ImageDescription
# Register your models here.

@admin.register(ImageDescription)
class ImageDescriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'size', 'created_at']
    list_filter = ['user', 'size', 'created_at']
    search_fields = ['user', 'size', 'description']

@admin.register(GeneratedImage)
class GeneratedImageAdmin(admin.ModelAdmin):
    list_display = ['description', 'image_url', 'is_active', 'created_at']
    list_filter = ['created_at', 'is_active']
    search_fields = ['description', 'image_url']

@admin.register(Trial)
class TrialAdmin(admin.ModelAdmin):
    list_display = ['user', 'number', 'created_at', 'updated_at']
    list_filter = ['user', 'created_at', 'updated_at']
