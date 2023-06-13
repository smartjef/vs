from django.contrib import admin
from .models import About, Testimony, Partner, FAQ, Category, Tag, Contact
# Register your models here.

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title','email', 'phone_number','address','is_active', 'created_at']

@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ['author', 'position', 'message', 'rating', 'is_active', 'created_at']
    list_filter = ['created_at', 'rating', 'is_active']
    search_fields = ['author_username', 'message', 'position']
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['title', 'website', 'logo', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'website']
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'is_active', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at', 'is_active']
    search_fields = ['question', 'answer']
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'phone_number', 'is_addressed', 'created_at')
    search_fields = ('name', 'subjec', 'email', 'phone_number')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_filter = ('created_at', 'is_addressed')