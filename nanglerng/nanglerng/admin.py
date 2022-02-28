from django.contrib import admin

from .models import Essay, Post, PostImage, Aboutus, TypePost, Tags

admin.site.register(Essay)
admin.site.register(TypePost)
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Aboutus)
admin.site.register(Tags)
