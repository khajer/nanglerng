from django.db import models
from django_quill.fields import QuillField
from taggit.managers import TaggableManager


class Essay(models.Model):
    imgCover = models.FileField(upload_to='media/%Y/%m/%d/', blank=True)
    txtIntro = models.CharField(max_length=200)
    rawHtmlData = QuillField()
    author = models.CharField(max_length=200)
    createAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.txtIntro

class Aboutus(models.Model):
    rawHtmlData = QuillField()
    author = models.CharField(max_length=200)
    createAt = models.DateTimeField(auto_now_add=True)

class TypePost(models.Model):
    typename = models.CharField(max_length=200)
    def __str__(self):
        return self.typename

class Post(models.Model):
    title = models.CharField(max_length=200)
    imgCover = models.FileField(upload_to='media/%Y/%m/%d/', blank=True)
    typePost = models.ForeignKey(TypePost, on_delete=models.CASCADE)
    eventTime = models.CharField(max_length=200)    
    eventDateTime = models.DateField(null=True, blank=True)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    desc = models.TextField()
    rawHtmlData = QuillField()
    category = models.CharField(max_length=200)
    contributor = models.CharField(max_length=200)    
    mainFlag = models.BooleanField(default=False)
    activeEvent = models.BooleanField(default=False)
    createAt = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ["-createAt"]

class PostImage(models.Model):
    image = models.FileField(upload_to='media/%Y/%m/%d/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)    
