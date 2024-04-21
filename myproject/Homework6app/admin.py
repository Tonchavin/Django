from django.contrib import admin
from .models import Category, Client, Product, Order


@admin.action(description="Сбросить количество в ноль")
def reset_value(modeladmin, request, queryset):
    queryset.update(value=0)


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов"""
    list_display = ['name', 'category', 'value', 'description', 'price', 'data', 'rating']
    list_filter = ['category', 'value', 'price', 'rating']
    ordering = ['-category', 'name']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта(description)'
    actions = [reset_value]

    """Отдельный продукт"""
    fields = ['name', 'category', 'value', 'description', 'price', 'data', 'date_add', 'rating']
    readonly_fields = ['date_add', 'rating']


class ClientAdmin(admin.ModelAdmin):
    """Список продуктов"""
    list_display = ['name', 'email', 'phone_number', 'address']
    list_filter = ['address']
    ordering = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Имя(name)'
    fields = ['name', 'email', 'phone_number', 'address', 'date_of_registry']
    readonly_fields = ['date_of_registry']


class OrderAdmin(admin.ModelAdmin):
    """Список продуктов"""
    list_display = ['client', 'total_amount', 'order_date']
    list_filter = ['order_date', 'total_amount', 'client']
    ordering = ['-order_date']
    search_fields = ['client', 'order_date', 'total_amount']
    search_help_text = 'Поиск по полю: client, total_amount, order_date'
    # fields = ['client', 'products', 'total_amount', 'order_date']
    readonly_fields = ['order_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['client'],
            },
        ),
        (
            'Product',
            {
                'classes': ['wide'],
                'fields': ['products'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробности Заказа',
                'fields': ['total_amount', 'order_date'],
            },
        ),
    ]


# Register your models here.
admin.site.register(Category)
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
