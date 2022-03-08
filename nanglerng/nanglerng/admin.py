from django.contrib import admin

from .models import Essay, Post, PostImage, Aboutus, TypePost

admin.site.register(TypePost)

admin.site.register(Aboutus)
# admin.site.register(Tags)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "typePost", "show_mainpage", "createAt",)    
    list_filter = ("typePost", )
    ordering = ('-createAt',)
    search_fields = ("title", )
    list_per_page = 20
    
    def show_mainpage(self, obj):
        return "show" if obj.mainFlag else ""
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["rawHtmlData"].label = "Content:"
        form.base_fields["imgCover"].label = "Image Cover:"
        form.base_fields["typePost"].label = "Type:"
        form.base_fields["mainFlag"].label = "Show MainPage"
        form.base_fields["desc"].label = "Short Description"
        return form
        

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ("post", "get_post_image", "image", "show_mainpage")
    def get_post_image(self, obj):
        return obj.post.typePost
    def show_mainpage(self, obj):
        return "Y" if obj.post.mainFlag else ""

@admin.register(Essay)
class EssayAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["txtIntro"].label = "Text Intro:"
        form.base_fields["rawHtmlData"].label = "Content:"
        form.base_fields["imgCover"].label = "Image Cover:"
        return form

