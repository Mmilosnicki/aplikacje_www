import graphene
from graphene_django import DjangoObjectType
from testapp.models import *


class OsobaType(DjangoObjectType):
    class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko', 'plec', 'stanowisko', 'data_dodania']


class StanowiskoType(DjangoObjectType):
    class Meta:
        model = Stanowisko
        fields = ['id', 'nazwa', 'opis']


class Query(graphene.ObjectType):
    wszystkie_osoby = graphene.List(OsobaType)
    osoba_by_id = graphene.Field(OsobaType, id=graphene.Int(required=True))
    wszystkie_stanowiska = graphene.List(StanowiskoType)
    stanowisko_by_id = graphene.Field(StanowiskoType, id=graphene.Int(required=True))
    osoba_by_imie = graphene.Field(OsobaType, imie=graphene.String(required=True))

    def resolve_wszystkie_osoby(root, info):
        return Osoba.objects.all()

    def resolve_osoba_by_id(root, info, id):
        try:
            return  Osoba.objects.get(pk=id)
        except Osoba.DoesNotExist:
            raise Exception("Nie ma osoby z takim id")

    def resolve_wszystkie_stanowiska(root, info):
        return Stanowisko.objects.all()

    def resolve_stanowisko_by_id(root, info, id):
        try:
            return Stanowisko.objects.get(pk=id)
        except Stanowisko.DoesNotExist:
            raise Exception("Nie ma stanowiska z takim id")

    def resolve_osoba_by_imie(root, info, imie):
        try:
            return Osoba.objects.get(imie=imie)
        except Osoba.DoesNotExist:
            raise Exception("Osoba o taikm imieniu nie istnieje w bazie")


schema = graphene.Schema(query=Query)