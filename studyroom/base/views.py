from django.shortcuts import render


rooms = [
    {"id": 1, "name": "let learn python!"},
    {"id": 2, "name": "backend dev!"},
    {"id": 3, "name": "desing ui/ux!"},
    {"id": 4, "name": "learning rust!"},
]


def home(request):
    return render(request, "base/home.html")


def room(request):
    return render(request, "base/rom.html", {'rooms': rooms})
