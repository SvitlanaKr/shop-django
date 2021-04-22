from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def goods(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Goods</h1>")
