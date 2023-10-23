```python

from testapp.models import * 
Osoba.objects.all()
<QuerySet [<Osoba: Jan Janusz>, <Osoba: Anna Kisiel>, <Osoba: Adam Nowak>]>

Osoba.objects.filter(id=3)
<QuerySet [<Osoba: Anna Kisiel>]>

Osoba.objects.filter(imie__startswith='J')
<QuerySet [<Osoba: Jan Janusz>]>

Osoba.objects.values('stanowisko').distinct()
<QuerySet [{'stanowisko': 2}, {'stanowisko': 3}, {'stanowisko': 1}]>

Stanowisko.objects.values('nazwa').order_by('-nazwa') 
<QuerySet [{'nazwa': 'Księgowa'}, {'nazwa': 'Kierownik'}, {'nazwa': 'Kierowca'}]>

osoba = Osoba(imie='Kamil', nazwisko='Marah', plec='1', stanowisko=Stanowisko.objects.get(id=1))         
osoba.save() 

```