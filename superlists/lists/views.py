from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    template = "home.html"
    return render(request, template)