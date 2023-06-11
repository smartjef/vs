from django.contrib import admin
from .models import Service, ServiceFAQ
# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'slug', 'created_at', 'updated_at']
    search_fields = ['title', 'description', 'slug']
    list_filter = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at',]

@admin.register(ServiceFAQ)
class ServiceFAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'service', 'is_active', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at', 'is_active', 'service']
    search_fields = ['question', 'answer', 'service']
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)