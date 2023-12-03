from django.test import TestCase
from ..models import *


class OsobaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Osoba.objects.create(imie='Andrzej', nazwisko='Andrzejek', plec=1)

    def test_first_name_label(self):
        osoba = Osoba.objects.get(id=1)
        field_label = osoba._meta.get_field('imie').verbose_name
        self.assertEqual(field_label, 'imie')

    def test_first_name_max_length(self):
        osoba = Osoba.objects.get(id=1)
        max_length = osoba._meta.get_field('imie').max_length
        self.assertEqual(max_length, 30)


class StanowiskoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.stanowisko1 = Stanowisko.objects.create(nazwa='Murarz', opis='Muruje')
        cls.stanowisko2 = Stanowisko.objects.create(nazwa='Tynkarz', opis='Tynkuje')

    def test_generating_id(self):
        self.assertNotEqual(self.stanowisko1.id, self.stanowisko2.id)

        self.assertEqual(self.stanowisko1.id + 1, self.stanowisko2.id)

    def test_opis_max_length(self):
        max_length = self.stanowisko1._meta.get_field('opis').max_length
        self.assertEqual(max_length, 100)