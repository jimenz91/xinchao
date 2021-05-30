from django.contrib import admin
from profiles.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email',)


admin.site.register(Client, ClientAdmin)
