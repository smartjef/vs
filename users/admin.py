from django.contrib import admin
from .models import Profile, Team, Skill
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','gender', 'phone_number','language_preference','linkedin', 'created_at']
    list_filter = ('gender','language_preference', 'created_at', 'updated_at')
    search_fields = ('user__username', 'user__email')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['order', 'user', 'slug', 'rank', 'is_active', 'created_at']
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('user__username', 'user__email', 'rank')
    date_hierarchy = 'created_at'
    ordering = ('order','-created_at')
    
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['team_member', 'title', 'level']
    list_filter = ['team_member', 'title', 'level']
    search_fields = ['team_member', 'title', 'level']