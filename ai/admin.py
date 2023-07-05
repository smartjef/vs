from django.contrib import admin
from .models import GeneratedImage, Trial
# Register your models here.

@admin.register(GeneratedImage)
class GeneratedImageAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'image_url', 'is_active', 'created_at']
    list_filter = ['user', 'created_at', 'is_active']
    search_fields = ['user', 'description', 'image_url']
    list_per_page = 10

@admin.register(Trial)
class TrialAdmin(admin.ModelAdmin):
    list_display = ['user', 'number', 'created_at', 'updated_at']
    list_filter = ['user', 'created_at', 'updated_at']
    search_fields = ['user', 'number']
    list_per_page = 10