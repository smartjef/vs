from django.contrib import admin
from .models import Referal, Period, AssignmentOrder, ProjectOrder, ProjectPeriod, AssignmentFiles, ProjectFiles, Payment
# Register your models here.

@admin.register(Referal)
class ReferalAdmin(admin.ModelAdmin):
    list_display = ['code', 'user', 'earnings', 'withdrawals', 'balance']
    autocomplete_fields = ['user',]
    search_fields = ['code', 'earnings', 'withdrawals', 'balance', 'user']
    list_filter = ['user',]

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ['quantity', 'unit', 'is_active', 'rate', 'created_at']
    search_fields = ['quantity', 'unit', 'rate']
    list_filter = ['is_active', 'created_at']

class AssignmentFilesInline(admin.TabularInline):
    model = AssignmentFiles
    extra = 0
    show_change_link = True
    fields = ('assignment', 'file')

class ProjectFilesInline(admin.TabularInline):
    model = ProjectFiles
    extra = 0
    show_change_link = True
    fields = ('project', 'file')

@admin.register(AssignmentOrder)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'academic_level', 'subject_area', 'period', 'status', 'refered_by', 'created_at', 'updated_at']
    search_fields = ['title', 'period',]
    autocomplete_fields = ['academic_level', 'subject_area', 'period', 'user', 'refered_by']
    list_filter = ['status', 'updated_at', 'academic_level', 'period', 'created_at']
    inlines = [AssignmentFilesInline]

@admin.register(ProjectPeriod)
class ProjectPeriodAdmin(admin.ModelAdmin):
    list_display = ['period', 'created_at', 'rate', 'updated_at']
    search_fields = ['period',]
    autocomplete_fields = ['period']
    list_filter = ['updated_at', 'period', 'created_at']

@admin.register(ProjectOrder)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'academic_level', 'subject_area', 'period', 'status', 'refered_by', 'created_at', 'updated_at']
    search_fields = ['title', 'period',]
    autocomplete_fields = ['academic_level', 'subject_area', 'period', 'user', 'refered_by']
    list_filter = ['status', 'updated_at', 'academic_level', 'period', 'created_at']
    inlines = [ProjectFilesInline]

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['transaction_code', 'project', 'assignment', 'amount', 'mpesa_code', 'is_paid', 'created_at']
    list_filter = ['is_paid', 'created_at']
    search_fields = ['transaction_code', 'project', 'assignment', 'amount', 'mpesa_code', 'description',]
    autocomplete_fields = ['project','assignment']