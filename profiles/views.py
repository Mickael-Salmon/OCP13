from django.shortcuts import render
from profiles.models import Profile

def profiles_index(request):
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles_index.html", context)

def profile(request, username):
    """
    View function that retrieves a user's profile based on their username and renders it to the profile.html template.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user whose profile is being requested.

    Returns:
        HttpResponse: The HTTP response object containing the rendered profile.html template.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profile.html", context)
