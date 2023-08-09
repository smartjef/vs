from django.contrib import admin
from .models import Referal, Period, AssignmentOrder, ProjectOrder, ProjectPeriod, AssignmentFiles, ProjectFiles, Payment, Response
# Register your models here.

@admin.register(Referal)
class ReferalAdmin(admin.ModelAdmin):
    list_display = ['code', 'user', 'earnings', 'withdrawals', 'balance']
    autocomplete_fields = ['user',]
    search_fields = ['code', 'earnings', 'withdrawals', 'balance', 'user']
    list_filter = ['user',]
    list_per_page = 20

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ['quantity', 'unit', 'is_active', 'rate', 'created_at']
    search_fields = ['quantity', 'unit', 'rate']
    list_filter = ['is_active', 'created_at']
    list_per_page = 20

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
    readonly_fields = ['refered_by',]
    list_per_page = 20

@admin.register(ProjectPeriod)
class ProjectPeriodAdmin(admin.ModelAdmin):
    list_display = ['period', 'created_at', 'rate', 'updated_at']
    search_fields = ['period',]
    autocomplete_fields = ['period']
    list_filter = ['updated_at', 'period', 'created_at']
    list_per_page = 20

@admin.register(ProjectOrder)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'academic_level', 'subject_area', 'period', 'status', 'refered_by', 'created_at', 'updated_at']
    search_fields = ['title', 'period',]
    autocomplete_fields = ['academic_level', 'subject_area', 'period', 'user', 'refered_by']
    list_filter = ['status', 'updated_at', 'academic_level', 'period', 'created_at']
    inlines = [ProjectFilesInline]
    readonly_fields = ['refered_by',]
    list_per_page = 20

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['transaction_code', 'project', 'assignment', 'amount', 'mpesa_code', 'description', 'is_paid', 'created_at']
    list_filter = ['is_paid', 'created_at']
    search_fields = ['transaction_code', 'project', 'assignment', 'amount', 'mpesa_code', 'description',]
    autocomplete_fields = ['project','assignment']
    readonly_fields = ['is_paid', 'transaction_code']
    actions = ['mark_as_paid', 'mark_as_unpaid']
    list_per_page = 20
    
    def mark_as_unpaid(self, request, queryset):
        queryset.update(is_paid=False)

    def mark_as_paid(self, request, queryset):
        queryset.update(is_paid=True)

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ['link', 'project', 'assignment', 'updated_at', 'created_at']
    list_filter = ['updated_at', 'created_at']
    search_fields = ['link', 'project', 'assignment',]
    autocomplete_fields = ['project','assignment']
    list_per_page = 20