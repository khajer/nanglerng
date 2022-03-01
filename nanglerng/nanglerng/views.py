from django.http import HttpResponse
from django.template import loader
from .models import Essay, Aboutus, Post

def index(request):
    template = loader.get_template('home/index.html')
    essay = Essay.objects.all()[0]    
    whatsons = Post.objects.all().filter(mainFlag=True, typePost="1")
    # locations = Post.objects.all().filter(mainFlag=True, typePost="2")
    location = Post.objects.all().filter(mainFlag=True, typePost="2")[0]
    articles = Post.objects.all().filter(mainFlag=True, typePost="3")
    context = {
        'essay': essay, 
        'whatsons': whatsons,
        'location': location,
        'articles': articles
    }
    return HttpResponse(template.render(context, request))

def comEssay(request):
    template = loader.get_template('community/essay.html')
    essay = Essay.objects.all()[0]    
    context = {'essay': essay}
    return HttpResponse(template.render(context, request))

def comTimeline(request, eventId=0):
    template = loader.get_template('community/timeline.html')
    context = {}
    return HttpResponse(template.render(context, request))

def comMap(request):
    template = loader.get_template('community/map.html')
    context = {}
    return HttpResponse(template.render(context, request))

def comMapLoc(request, locId=0):
    template = loader.get_template('community/mapLoc.html')
    context = {}
    return HttpResponse(template.render(context, request))

def whatsOn(request):
    template = loader.get_template('whatson/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def article(request):
    template = loader.get_template('article/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def articleDetail(request, articleId=0):
    template = loader.get_template('article/detail.html')
    articles = Post.objects.all().filter(id=articleId)
    context = {
        "article":articles[0]
    }
    return HttpResponse(template.render(context, request))

def aboutus(request):
    template = loader.get_template('aboutus/index.html')
    aboutus = Aboutus.objects.all()[0]    
    context = {'aboutus':aboutus}    
    return HttpResponse(template.render(context, request))

def tags(request):
    template = loader.get_template('tags/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
