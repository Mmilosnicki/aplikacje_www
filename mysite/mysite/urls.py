from django.urls import path, include
from django.contrib import admin
from testapp import views
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('osoba/<int:pk>/', views.osoba_view),
    path('dodaj_osobe/', views.dodaj_osobe),
    path('lista_osob/', views.lista_osob),
    path('lista_osob_filter/', views.lista_osob_filter),
    path('stanowisko/<int:pk>/', views.stanowisko),
    path('dodaj_stanowisko/', views.dodaj_stanowisko),
    path('lista_stanowisk/', views.lista_stanowisk),
    path('osoba_update/<int:pk>', views.osoba_update_delete),
    path('osoba_delete/<int:pk>', views.osoba_update_delete),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]