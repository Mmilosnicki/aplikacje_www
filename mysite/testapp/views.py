from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied


@permission_required('testapp.view_osoba')
def osoba_view(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
        return HttpResponse(f"Ten użytkownik nazywa się {osoba.imie}")
    except Osoba.DoesNotExist:
        return HttpResponse(f"W bazie nie ma użytkownika o id={pk}.")


@api_view(['GET'])
def osoba(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        osoba = Osoba.objects.get(pk=pk)
        serializer = OsobaModelSerializer(osoba)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_update_delete(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OsobaModelSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def dodaj_osobe(request):
    if request.method == 'POST':
        serializer = OsobaModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(wlasciciel=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def lista_osob(request):
    if request.method == 'GET':
        osoby = Osoba.objects.all()
        serializer = OsobaModelSerializer(osoby, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def lista_osob_filter(request):
    if request.method == 'GET':
        search_param = request.query_params.get('search', '')
        osoby = Osoba.objects.filter(imie__icontains=search_param)
        serializer = OsobaModelSerializer(osoby, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def stanowisko(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        stanowisko = Stanowisko.objects.get(pk=pk)
        serializer = StanowiskoSerializer(stanowisko)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def dodaj_stanowisko(request):
    if request.method == 'POST':
        stanowisko = Stanowisko()
        serializer = StanowiskoSerializer(stanowisko, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def lista_stanowisk(request):
    if request.method == 'GET':
        stanowiska = Stanowisko.objects.all()
        serializer = StanowiskoSerializer(stanowiska, many=True)
        return Response(serializer.data)