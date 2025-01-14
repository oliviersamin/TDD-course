from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item


def home_page(request):
    template = "home.html"
    if request.method == "POST":
        Item.objects.create(text=request.POST.get("item_text"))
        return redirect('/')

    context = {"items": [item for item in Item.objects.all()]}

    return render(
        request,
        template,
        context=context
    )