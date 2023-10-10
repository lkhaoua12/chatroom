from django.shortcuts import render


rooms = [
    {"id": 1, "name": "let learn python!"},
    {"id": 2, "name": "backend dev!"},
    {"id": 3, "name": "desing ui/ux!"},
    {"id": 4, "name": "learning rust!"},
]


def home(request):
    return render(request, "base/home.html", {'rooms': rooms})


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    return render(request, "base/rom.html", {"room": room})
