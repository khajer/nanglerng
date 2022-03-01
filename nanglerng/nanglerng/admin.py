from django.contrib import admin

from .models import Essay, Post, PostImage, Aboutus, TypePost, Tags

# admin.site.register(Essay)
admin.site.register(TypePost)

admin.site.register(Aboutus)
admin.site.register(Tags)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "typePost", "createAt", "show_mainpage")    
    def show_mainpage(self, obj):
        return "show" if obj.mainFlag else ""

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ("post", "get_post_image", "image")
    def get_post_image(self, obj):
        return obj.post.typePost
   

@admin.register(Essay)
class EssayAdmin(admin.ModelAdmin):
    pass 
