from django.urls import path, include
from django.contrib import admin
from testapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('osoba/<int:pk>/', views.osoba),
    path('dodaj_osobe/', views.dodaj_osobe),
    path('lista_osob/', views.lista_osob),
    path('lista_osob_filter/', views.lista_osob_filter),
    path('stanowisko/<int:pk>/', views.stanowisko),
    path('dodaj_stanowisko/', views.dodaj_stanowisko),
    path('lista_stanowisk/', views.lista_stanowisk),
]
