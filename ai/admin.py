from django.contrib import admin
from .models import GeneratedImage, Trial, ImageDescription
# Register your models here.

class GeneratedImageInline(admin.TabularInline):
    model = GeneratedImage
    extra = 0
    show_change_link = True
    fields = ('image_url', 'is_active', 'created_at')
    readonly_fields = ('image_url', 'created_at')
    ordering = ('-created_at',)

@admin.register(ImageDescription)
class ImageDescriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'size', 'created_at']
    list_filter = ['user', 'size', 'created_at']
    search_fields = ['user', 'size', 'description']
    inlines = [GeneratedImageInline]

@admin.register(Trial)
class TrialAdmin(admin.ModelAdmin):
    list_display = ['user', 'number', 'created_at', 'updated_at']
    list_filter = ['user', 'created_at', 'updated_at']
