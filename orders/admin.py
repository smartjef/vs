from django.contrib import admin
from .models import Order, OrderItem
from django.urls import reverse
from django.utils.safestring import mark_safe
# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

def order_detail(obj):
    url = reverse('orders:admin_order_detail', args=[obj.id])
    return mark_safe(f'<a href="{url}">View</a>')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'paid', 'created_at', 'updated_at', order_detail]
    list_filter = ['paid', 'created_at', 'updated_at']
    inlines = [OrderItemInline]
    list_per_page = 20
    search_fields = ['id', 'user__username', 'first_name', 'last_name', 'email', 'address', 'postal_code']
    autocomplete_fields = ['user']
