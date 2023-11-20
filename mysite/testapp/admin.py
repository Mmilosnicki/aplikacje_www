from django.contrib import admin
from django.contrib import auth
from .models import *


class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ['data_dodania']
    list_display = ['imie', 'nazwisko', 'Stanowisko']
    list_filter = ['stanowisko', 'data_dodania']

    @admin.display(empty_value='')
    def Stanowisko(self, obj):
        if obj.stanowisko:
            return f"{obj.stanowisko.nazwa, obj.stanowisko.id}"
        else:
            return "Brak stanowiska"


class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ['nazwa']
    list_filter = ['nazwa']


admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko, StanowiskoAdmin)
