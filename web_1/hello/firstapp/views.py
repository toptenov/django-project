from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render


def index(request):
    header = "Персональные данные"
    langs = ["Английский", "Немецкий", "Испанский"]
    user = {"name": "Максим,", "age": 30}
    addr = ("Виноградная", 23, 45)
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return render(request, "index.html", context=data)


def about(request):
    return HttpResponse("About")


def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")


def products(request, productid):
    category = request.GET.get("cat", "")
    output = f"<h2>Продукт № {productid} Категория: {category}</h2>"
    return HttpResponse(output)


def users(request):
    id = request.GET .get("id", 1)
    name = request.GET.get("name", "Максим")
    output = f"<h2>Пользователь</h2><hЗ>id: {id} Имя: {name}</hЗ >"
    return HttpResponse(output)
