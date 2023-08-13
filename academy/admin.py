from django.contrib import admin
from .models import School, UnitName, Note
# Register your models here.

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'logo', 'is_active']
    list_filter = ['is_active', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)} 
    search_fields = ['title',]

@admin.register(UnitName)
class UNitNameAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active']
    list_filter = ['is_active', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)} 
    search_fields = ['title']

@admin.register(Note)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'unit_name', 'school', 'is_active']
    list_filter = ['is_active', 'created_at', 'updated_at']
    autocomplete_fields = ['unit_name', 'school', 'user']
    search_fields = ['file']
 