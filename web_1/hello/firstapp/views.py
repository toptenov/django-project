from django.shortcuts import render

from firstapp.forms import UserForm


def index(request):
    userform = UserForm()
    return render(request, "firstapp/index.html", {"form": userform})
