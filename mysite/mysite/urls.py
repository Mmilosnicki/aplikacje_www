from django.urls import path, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from testapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('osoba/<int:pk>/', views.DanaOsoba.as_view()),
    path('dodaj_osobe/', views.DodajOsobe.as_view()),
    path('lista_osob/', views.ListaOsob.as_view()),
    path('lista_osob_filter/', views.ListaOsobFilter.as_view()),
]
