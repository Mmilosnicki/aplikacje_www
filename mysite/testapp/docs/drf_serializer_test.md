```python

>>> from testapp.models import *
>>> from testapp.serializers import *
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser

>>> osoba = Osoba(imie='Piotr', nazwisko='Kobra', plec=1, stanowisko=Stanowisko.objects.get(id=2))
>>> osoba.save()

>>> serializer = OsobaModelSerializer(osoba)
>>> serializer.data  
{'id': 5, 'imie': 'Piotr', 'nazwisko': 'Kobra', 'plec': 1, 'stanowisko': 2, 'data_dodania': '2023-10-30'}

>>> content = JSONRenderer().render(serializer.data)
>>> content
b'{"id":5,"imie":"Piotr","nazwisko":"Kobra","plec":1,"stanowisko":2,"data_dodania":"2023-10-30"}'

>>> import io
>>> stream = io.BytesIO(content)
>>> data = JSONParser().parse(stream)
>>> deserializer = OsobaModelSerializer(data=data)
>>> deserializer.is_valid()
True

>>> deserializer.fields
{'id': IntegerField(label='ID', read_only=True), 'imie': CharField(max_length=30), 'nazwisko': CharField(max_length=30), 'plec': ChoiceField(choices=[(1, 'Mezczyzna'), (2, 'Kobieta'), (3, 'Inne')]), 'stanowisko': PrimaryKeyRelatedField(allow_null=True, queryset=Stan
owisko.objects.all(), required=False), 'data_dodania': DateField(read_only=True)}

>>> deserializer.validated_data
OrderedDict([('imie', 'Piotr'), ('nazwisko', 'Kobra'), ('plec', 1), ('stanowisko', <Stanowisko: Stanowisko object (2)>)])

>>> deserializer.save()
<Osoba: Piotr Kobra>
>>> deserializer.data
{'id': 6, 'imie': 'Piotr', 'nazwisko': 'Kobra', 'plec': 1, 'stanowisko': 2, 'data_dodania': '2023-10-30'}

---------------------------------------------------------------------------------------------------------------------------

>>> stanowisko = Stanowisko(nazwa='Kasjer')      
>>> stanowisko.save()

>>> serializer = StanowiskoSerializer(stanowisko)
>>> serializer.data
{'nazwa': 'Kasjer', 'opis': None}

>>> content = JSONRenderer().render(serializer.data)
>>> content
b'{"nazwa":"Kasjer","opis":null}'

>>> stream = io.BytesIO(content)
>>> data = JSONParser().parse(stream)
>>> deserializer = StanowiskoSerializer(data=data) 
>>> deserializer.is_valid()
True

>>> deserializer.fields
{'nazwa': CharField(max_length=30, required=True), 'opis': CharField(allow_null=True, max_length=100, required=False)}

>>> deserializer.validated_data
OrderedDict([('nazwa', 'Magazynier'), ('opis', None)])

>>> deserializer.save()
<Stanowisko: Stanowisko object (8)>

```