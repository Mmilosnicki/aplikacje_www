from rest_framework import serializers
from .models import *


class StanowiskoSerializer(serializers.Serializer):
    nazwa = serializers.CharField(required=True, max_length=30)
    opis = serializers.CharField(required=False, max_length=100, allow_null=True)

    def create(self, validated_data):
        return Stanowisko.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.save()
        return instance


class OsobaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko', 'plec', 'stanowisko', 'data_dodania']

