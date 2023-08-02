from django.contrib import admin
from .models import GeneratedImage, Trial, ImageDescription, AreaChoice, LevelChoice, IdeaRequest, GeneratedIdeas, Payment
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
    autocomplete_fields = ['user',]
    inlines = [GeneratedImageInline]

@admin.register(Trial)
class TrialAdmin(admin.ModelAdmin):
    list_display = ['user', 'image_trial', 'ideas_trial', 'created_at', 'updated_at']
    list_filter = ['user', 'created_at', 'updated_at']
    autocomplete_fields = ['user',]
    search_fields = ['user', 'image_url', 'image_trial', 'ideas_trial']

@admin.register(AreaChoice)
class AreaChoiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'craeted_at']
    list_filter = ['craeted_at']
    search_fields = ['title', 'description']

@admin.register(LevelChoice)
class LevelChoiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'charge_rate', 'craeted_at']
    list_filter = ['craeted_at']
    search_fields = ['title', 'description', 'charge_rate']

class GeneratedIdeasInline(admin.TabularInline):
    model = GeneratedIdeas
    extra = 0
    show_change_link = True
    fields = ('id', 'title', 'description', 'created_at')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

@admin.register(IdeaRequest)
class IdeaRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'area', 'level', 'number_of_ideas', 'is_active', 'refered_by', 'created_at']
    list_filter = ['user', 'area', 'level', 'created_at', 'refered_by', 'is_active']
    search_fields = ['user', 'refered_by', 'description', 'area', 'level', 'number_of_ideas']
    autocomplete_fields = ['user', 'area', 'level', 'refered_by']
    inlines = [GeneratedIdeasInline]
    readonly_fields = ['refered_by',]

@admin.register(Payment)
class IdeaPaymentAdmin(admin.ModelAdmin):
    list_display = ['transaction_code', 'idea_request', 'amount', 'mpesa_code', 'is_paid', 'created_at']
    list_filter = ['is_paid', 'created_at']
    search_fields = ['transaction_code', 'amount', 'mpesa_code', 'description', 'idea_request_area', 'idea_request_level']
    autocomplete_fields = ['idea_request',]
    readonly_fields = ['is_paid', 'transaction_code']
    actions = ['mark_as_paid', 'mark_as_unpaid']

    def mark_as_unpaid(self, request, queryset):
        queryset.update(is_paid=False)

    def mark_as_paid(self, request, queryset):
        queryset.update(is_paid=True)
