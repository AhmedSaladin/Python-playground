from django.contrib import admin
from .models import Profile

# adding profile table to admin page.
admin.site.register(Profile)
