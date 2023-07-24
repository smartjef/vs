from django.contrib import admin
from .models import GeneratedImage, Trial, ImageDescription, AreaChoice, LevelChoice, IdeaRequest, GeneratedIdeas
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
    list_display = ['user', 'image_trial', 'ideas_trial', 'created_at', 'updated_at']
    list_filter = ['user', 'created_at', 'updated_at']

@admin.register(AreaChoice)
class AreaChoiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'craeted_at']
    list_filter = ['craeted_at']
    search_fields = ['title']

@admin.register(LevelChoice)
class LevelChoiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'craeted_at']
    list_filter = ['craeted_at']
    search_fields = ['title']

class GeneratedIdeasInline(admin.TabularInline):
    model = GeneratedIdeas
    extra = 0
    show_change_link = True
    fields = ('project_title', 'project_details', 'created_at')
    readonly_fields = ('project_title', 'project_details', 'created_at')
    ordering = ('-created_at',)

@admin.register(IdeaRequest)
class IdeaRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'area', 'level', 'created_at']
    list_filter = ['user', 'area', 'level', 'created_at']
    search_fields = ['user', 'description']
    inlines = [GeneratedIdeasInline]
