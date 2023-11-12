from rest_framework import serializers
from .models import *


class StanowiskoSerializer(serializers.Serializer):
    nazwa = serializers.CharField(required=True, max_length=30)
    opis = serializers.CharField(required=False, max_length=100, allow_null=True, allow_blank=True)

    def create(self, validated_data):
        return Stanowisko.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.save()
        return instance


class OsobaModelSerializer(serializers.ModelSerializer):
    def validate_imie(self, value):
        if not value.isalpha():
            raise serializers.ValidationError('Imie może zawierać tylko litery.')
        return value

    def validate_data_dodania(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError('Data nie moze być z przyszłości')
        return value

    class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko', 'plec', 'stanowisko', 'data_dodania']

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.plec = validated_data.get('plec', instance.plec)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.data_dodania = validated_data.get('data_dodania', instance.data_dodania)
        instance.save()
        return instance
