from django.contrib import admin
from .models import GeneratedImage, Trial, ImageDescription, AreaChoice, LevelChoice, IdeaRequest, GeneratedIdeas, Payment, IdeaPool, IdeaPoolCategory
# Register your models here.
from decimal import Decimal
from assignments.models import Referal
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
    list_per_page = 20

@admin.register(Trial)
class TrialAdmin(admin.ModelAdmin):
    list_display = ['user', 'image_trial', 'ideas_trial', 'created_at', 'updated_at']
    list_filter = ['user', 'created_at', 'updated_at']
    autocomplete_fields = ['user',]
    search_fields = ['user', 'image_url', 'image_trial', 'ideas_trial']
    list_per_page = 20

@admin.register(AreaChoice)
class AreaChoiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'craeted_at']
    list_filter = ['craeted_at']
    search_fields = ['title', 'description']
    list_per_page = 20

@admin.register(LevelChoice)
class LevelChoiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'charge_rate', 'craeted_at']
    list_filter = ['craeted_at']
    search_fields = ['title', 'description', 'charge_rate']
    list_per_page = 20

class GeneratedIdeasInline(admin.TabularInline):
    model = GeneratedIdeas
    extra = 0
    show_change_link = True
    autocomplete_fields = ['idea',]
    fields = ('idea', 'created_at')
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
    list_per_page = 20

@admin.register(Payment)
class IdeaPaymentAdmin(admin.ModelAdmin):
    list_display = ['transaction_code', 'idea_request', 'amount', 'mpesa_code', 'is_paid', 'created_at']
    list_filter = ['is_paid', 'created_at']
    search_fields = ['transaction_code', 'amount', 'mpesa_code', 'description', 'idea_request_area', 'idea_request_level']
    autocomplete_fields = ['idea_request',]
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

        if payment.idea_request:
            referer = payment.idea_request.refered_by

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

@admin.register(IdeaPoolCategory)
class IdeaPoolCategoryAdmin(admin.ModelAdmin):
    list_display = ['academic_level', 'subject_area', 'created_at']
    list_filter = ['academic_level', 'subject_area']
    search_fields = ['academic_level', 'subject_area']
    autocomplete_fields = ['academic_level', 'subject_area']
    list_per_page = 20

@admin.register(IdeaPool)
class IdeaPoolAdmin(admin.ModelAdmin):
    list_display = ['title', 'pool_category', 'created_at']
    list_filter = ['pool_category', 'created_at']
    search_fields = ['title', 'description']
    autocomplete_fields = ['pool_category']
    list_per_page = 20
