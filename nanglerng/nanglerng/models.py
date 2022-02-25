from django.db import models
from django_quill.fields import QuillField

class Essay(models.Model):
    imgCover = models.FileField(upload_to='media/%Y/%m/%d/')
    txtIntro = models.CharField(max_length=200)
    rawHtmlData = QuillField()
    author = models.CharField(max_length=200)
    createAt = models.DateTimeField(auto_now_add=True)

