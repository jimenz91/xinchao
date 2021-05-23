from django.contrib import admin
from .models import Dish, Table, Order


class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'weight', 'rations_available')
    list_display_links = ('id', 'name')
    list_filter = ('rations_available',)


class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'availability')
    list_editable = ('availability',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'diners', 'table_id', 'time')


admin.site.register(Dish, DishAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Order, OrderAdmin)
