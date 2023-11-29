from django.contrib import admin

from letting.models import Letting
from letting.models import Address
from profiles.models import Profile


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
