from django.shortcuts import render


def index(request):
    """
    Renders the index page of the website.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response.
    """
    # logique de la vue
    return render(request, "index.html")
