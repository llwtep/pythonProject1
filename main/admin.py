from django.contrib import admin
from .models import Post, LikesOfThePost

admin.site.register(Post)
admin.site.register(LikesOfThePost)

