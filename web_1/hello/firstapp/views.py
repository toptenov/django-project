from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Глaвнaя</h2>")


def about(request):
    return HttpResponse("<h2>0 сайте</h2>")


def contact(request):
    return HttpResponse("<h2>Koнтaкты</h2>")


def products(request, productid):
    category = request.GET.get("cat", "")
    output = f"<h2>Продукт № {productid} Категория: {category}</h2>"
    return HttpResponse(output)


def users(request):
    id = request.GET .get("id", 1)
    name = request.GET.get("name", "Максим")
    output = f"<h2>Пользователь</h2><hЗ>id: {id} Имя: {name}</hЗ >"
    return HttpResponse(output)
