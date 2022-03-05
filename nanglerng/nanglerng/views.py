from django.http import HttpResponse
from django.template import loader
from .models import Essay, Aboutus, Post, TypePost

def index(request):
    template = loader.get_template('home/index.html')
    essay = Essay.objects.all()[0]    
    whatsons = Post.objects.all().filter(mainFlag=True, typePost="1")
    # locations = Post.objects.all().filter(mainFlag=True, typePost="2")
    location = Post.objects.all().filter(mainFlag=True, typePost="2").order_by('id').reverse()[0]
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
    typePost = TypePost.objects.filter(typename="Event")[0]
    events = Post.objects.all().filter(mainFlag=True, typePost=typePost.id).order_by('id').reverse()

    event = None
    if eventId == 0:
        event = events[0]
    else:
        event = list(filter(lambda e: (e.id == eventId), events))[0]
    
    context = {
        "events": events,
        "event": event

    }
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
    context = {}
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
