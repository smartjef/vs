from django.contrib import admin
from .models import Subscriber, MailMessage
# Register your models here.

@admin.register(Subscriber)
class SubcriberAdmin(admin.ModelAdmin):
    list_display = ('email','name', 'is_subscribed', 'created_at', 'updated_at')
    list_filter = ('is_subscribed', 'created_at')
    search_fields = ('name','email')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

@admin.register(MailMessage)
class MailMessageAdmin(admin.ModelAdmin):
    list_display = ('subject','template', 'author', 'created_at', 'updated_at')
    list_filter = ('template', 'author')
    search_fields = ('subject','message')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'