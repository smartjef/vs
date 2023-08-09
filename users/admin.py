from django.contrib import admin
from .models import Profile, Team, Skill, Preferences
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class PreferencesInline(admin.StackedInline):
    model = Preferences
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, PreferencesInline)

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 5
    show_change_link = True
    fields = ('title', 'level')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['user', 'order', 'slug', 'rank', 'is_active', 'created_at']
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('user__username', 'user__email', 'rank')
    date_hierarchy = 'created_at'
    ordering = ('order','-created_at')
    inlines = [SkillInline]
    list_per_page = 10

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, PreferencesInline)
    list_per_page = 15

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)