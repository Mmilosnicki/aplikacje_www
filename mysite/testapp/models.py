from django.db import models
from django.utils import timezone


class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=30)
    opis = models.CharField(null=True, blank=True, max_length=100)


class Osoba(models.Model):
    class Plec(models.IntegerChoices):
        Mezczyzna = 1
        Kobieta = 2
        Inne = 3

    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    plec = models.IntegerField(choices=Plec.choices)
    stanowisko = models.ForeignKey(Stanowisko, null=True, blank=True, on_delete=models.DO_NOTHING)
    data_dodania = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['nazwisko']

    def __str__(self):
        return '%s %s' % (self.imie, self.nazwisko)
