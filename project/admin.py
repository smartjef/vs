from django.contrib import admin
from .models import Project
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'website', 'client', 'is_active', 'updated_at')
    list_filter = ('created_at','category', 'updated_at')
    search_fields = ('title', 'slug', 'category', 'description', 'client', 'website')
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at','updated_at')
    # readonly_fields = ('title', 'description', 'image', 'slug', 'created')
    # list_editable = ('icon', 'slug')
