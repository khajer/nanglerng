from django.contrib import admin

from .models import Essay, Post, PostImage, Aboutus, TypePost, Tags

# admin.site.register(Essay)
admin.site.register(TypePost)

admin.site.register(Aboutus)
admin.site.register(Tags)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "typePost", "createAt")    

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ("post", "image")

@admin.register(Essay)
class EssayAdmin(admin.ModelAdmin):
    pass 
