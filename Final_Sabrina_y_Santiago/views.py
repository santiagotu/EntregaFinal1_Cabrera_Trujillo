from django.http import HttpResponse
from django.shortcuts import render



def inicio(request):
    return HttpResponse("Entrega 1 proyecto final")

def artistas(request):
    return HttpResponse("Artistas")

def avaluadores(request):
    return HttpResponse("Avaluadores")

def obras(request):
    return HttpResponse("Obras")    