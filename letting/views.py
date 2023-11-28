from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from letting.models import Letting


def index(request):
    return render(request, "index.html")


def lettings_index(request):
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "letting/index.html", context)


# def letting(request, letting_id):
#     """
#     View function that retrieves a letting object with the given ID and renders it to the letting.html template.

#     Args:
#         request (HttpRequest): The HTTP request object.
#         letting_id (int): The ID of the letting object to retrieve.

#     Returns:
#         HttpResponse: The HTTP response object that contains the rendered letting.html template.
#     """
#     letting = Letting.objects.get(id=letting_id)
#     context = {
#         "title": letting.title,
#         "address": letting.address,
#     }
#     return render(request, "letting/letting.html", context)

def letting(request, letting_id):
    """
    View function that retrieves a letting object with the given ID and renders it to the letting.html template.
    If the letting object with the given ID does not exist, it returns a 404 response.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting object to retrieve.

    Returns:
        HttpResponse: The HTTP response object that contains the rendered letting.html template.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "letting/letting.html", context)
