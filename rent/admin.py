from django.contrib import admin
from .models import Client, City, Flat, Rent


class ClientAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'name', 'surname')


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Client, ClientAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Flat)
admin.site.register(Rent)
