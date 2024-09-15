from django.shortcuts import render
from django.http import HttpResponse


def shop_index(request):
    return HttpResponse("Hello, world. You're at the shop_index view.")
