from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1><marquee><font color=red>Hello, world. You're at the polls index.")


def hello(request):
    return HttpResponse("<h1><marquee><font color=red>This is when you call /hello")
