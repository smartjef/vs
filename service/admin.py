from django.contrib import admin
from .models import Service
# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'slug', 'created_at', 'updated_at']
    search_fields = ['title', 'description', 'slug']
    list_filter = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at',]