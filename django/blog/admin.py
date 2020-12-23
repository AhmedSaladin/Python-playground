from django.contrib import admin
from .models import Post

# Add Post table to admin page.
admin.site.register(Post)
