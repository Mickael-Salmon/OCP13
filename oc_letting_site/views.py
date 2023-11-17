from django.shortcuts import render


def index(request):
    # logique de la vue
    return render(request, "index.html")
