from django.contrib import admin
from django.urls import path, include
from oc_letting_site import views as main_views
from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path("", main_views.index, name="index"),
    path("lettings/", include("letting.urls")),
    path("profiles/", include("profiles.urls")),
    path('sentry-debug/', trigger_error),
    path("admin/", admin.site.urls),
]
