from django.contrib import admin
from django.urls import path, include
from letting import views as letting_views
from profiles import views as profile_views
from oc_letting_site import views as main_views

urlpatterns = [
    path("", main_views.index, name="index"),
    path("lettings/", include("letting.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
]
