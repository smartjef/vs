from django.contrib import admin
from .models import Post, Comment, Reply
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'author', 'views', 'likes', 'dislikes', 'is_published', 'published_date', 'created_at', 'updated_at')
    list_filter = ('category', 'author', 'is_published', 'published_date', 'created_at', 'updated_at')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)

class ReplyInline(admin.TabularInline):
    model = Reply
    extra = 1
    can_delete = False
    show_change_link = True
    fields = ('name', 'email', 'message', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'is_approved', 'created_at', 'updated_at')
    list_filter = ('is_approved', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'message')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    inlines = [ReplyInline]

