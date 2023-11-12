from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class DanaOsoba(APIView):
    def get_object(self, pk):
        try:
            return Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        osoba = self.get_object(pk)
        serializer = OsobaModelSerializer(osoba)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        osoba = self.get_object(pk)
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListaOsob(APIView):
    def get(self, request, format=None):
        osoby = Osoba.objects.all()
        serializer = OsobaModelSerializer(osoby, many=True)
        return Response(serializer.data)


class DodajOsobe(APIView):
    def post(self, request, format=None):
        serializer = OsobaModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListaOsobFilter(APIView):
    def get(self, request, format=None):
        search_param = request.query_params.get('search', '')
        osoby = Osoba.objects.filter(imie__icontains=search_param)
        serializer = OsobaModelSerializer(osoby, many=True)
        return Response(serializer.data)
