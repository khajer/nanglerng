from django.db import models
from django_quill.fields import QuillField

class Essay(models.Model):
    imgCover = models.FileField(upload_to='media/%Y/%m/%d/')
    txtIntro = models.CharField(max_length=200)
    rawHtmlData = QuillField()
    author = models.CharField(max_length=200)
    createAt = models.DateTimeField(auto_now_add=True)

class Aboutus(models.Model):
    rawHtmlData = QuillField()
    author = models.CharField(max_length=200)
    createAt = models.DateTimeField(auto_now_add=True)

class TypePost(models.Model):
    typename = models.CharField(max_length=200)

class Post(models.Model):
    title = models.CharField(max_length=200)
    typePost = models.ForeignKey(TypePost, on_delete=models.CASCADE)
    eventTime = models.CharField(max_length=200)    
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)    
    desc = models.TextField()
    rawHtmlData = QuillField()
    culture = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    contribute = models.CharField(max_length=200)
    main_flag = models.BooleanField(default=False)
    createAt = models.DateTimeField(auto_now_add=True)

class PostImage(models.Model):
    image = models.FileField(upload_to='media/%Y/%m/%d/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Tags(models.Model):
    word = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)