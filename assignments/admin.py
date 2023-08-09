from django.contrib import admin
from decimal import Decimal
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
        for payment in queryset:
            payment.is_paid = False
            payment.save()

            self.update_referer_earnings(payment, subtract=True)

        self.message_user(request, "Selected payments have been marked as unpaid.")

    def mark_as_paid(self, request, queryset):
        for payment in queryset:
            payment.is_paid = True
            payment.save()

            self.update_referer_earnings(payment, subtract=False)

        self.message_user(request, "Selected payments have been marked as paid.")

    def update_referer_earnings(self, payment, subtract=False):
        referer = None

        if payment.project:
            referer = payment.project.refered_by
        elif payment.assignment:
            referer = payment.assignment.refered_by

        if referer:
            referal_instance, created = Referal.objects.get_or_create(user=referer)

            if not subtract:
                amount_earned = Decimal(payment.get_amount_earned_by_referer())
                referal_instance.earnings += amount_earned
                referal_instance.balance += amount_earned
            else:
                amount_deducted = Decimal(payment.get_amount_earned_by_referer())
                referal_instance.earnings -= amount_deducted
                referal_instance.balance -= amount_deducted

            referal_instance.save()

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ['link', 'project', 'assignment', 'updated_at', 'created_at']
    list_filter = ['updated_at', 'created_at']
    search_fields = ['link', 'project', 'assignment',]
    autocomplete_fields = ['project','assignment']
    list_per_page = 20