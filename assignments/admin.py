from django.contrib import admin
from .models import Referal
# Register your models here.

@admin.register(Referal)
class ReferalAdmin(admin.ModelAdmin):
    list_display = ['code', 'user', 'earnings', 'withdrawals', 'balance']
    autocomplete_fields = ['user',]
    search_fields = ['code', 'earnings', 'withdrawals', 'balance', 'user']
    list_filter = ['user',]