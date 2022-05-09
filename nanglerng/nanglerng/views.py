from django.http import HttpResponse
from django.template import loader
from .models import Essay, Aboutus, Post, TypePost, PostImage
from taggit.models import Tag

TYPE_ARTICLE = "3"
TYPE_LOCATION = "2"
TYPE_EVENT = "1"

def index(request):
    template = loader.get_template('home/index.html')
    essay = Essay.objects.all()[0]    
    whatsons = Post.objects.all().filter(mainFlag = True, typePost = TYPE_EVENT)    
    location = Post.objects.all().filter(mainFlag = True, typePost = TYPE_LOCATION).order_by('id').reverse()[0]
    articles = Post.objects.all().filter(mainFlag = True, typePost = TYPE_ARTICLE)
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
    
    events = Post.objects.all().filter(typePost=typePost.id)
    event = None
    if eventId == 0:
        event = events[0]   
    else:
        event = list(filter(lambda e: (e.id == eventId), events))[0]
    
    postImgs = PostImage.objects.all().filter(post=event.id)

    context = {
        "events": events,
        "event": event,
        "postImgs": postImgs
    }
    return HttpResponse(template.render(context, request))

def comMap(request):
    template = loader.get_template('community/map.html')
    typePost = TypePost.objects.filter(typename="Location")[0]    
    locations = Post.objects.all().filter(typePost=typePost.id).order_by('id').reverse()    
    context = {
        "locations":locations
    }
    return HttpResponse(template.render(context, request))

def comMapLoc(request, locId=0):
    template = loader.get_template('community/mapLoc.html')
    typePost = TypePost.objects.filter(typename="Location")[0]    
    locations = Post.objects.all().filter(typePost=typePost.id).order_by('id').reverse()
    location = list(filter(lambda e: (e.id == locId), locations))[0]
    
    postImgs = PostImage.objects.all().filter(post=location.id)
    
    articles = Post.objects.all().filter(parent=location.id, typePost = TYPE_ARTICLE).order_by('id').reverse()
    events = Post.objects.all().filter(parent=location.id, typePost = TYPE_EVENT).order_by('id').reverse()

    context = {
        "locations": locations,
        "location": location,
        "postImgs": postImgs,
        "events": events,
        "articles": articles
    }
    return HttpResponse(template.render(context, request))

def whatsOn(request):
    template = loader.get_template('whatson/index.html')
    typePost = TypePost.objects.filter(typename="Event")[0]
    events = Post.objects.all().filter(activeEvent=True, typePost=typePost.id).order_by('id').reverse()
    context = {
        "events": events
    }
    return HttpResponse(template.render(context, request))

def article(request):
    template = loader.get_template('article/index.html')
    typePost = TypePost.objects.filter(typename = "Article")[0]
    articles = Post.objects.all().filter(typePost=typePost.id).order_by('id').reverse()
    context = {
        "articles": articles
    }
    return HttpResponse(template.render(context, request))

def articleDetail(request, articleId=0):
    template = loader.get_template('article/detail.html')
    article = Post.objects.get(id=articleId)
    context = {"article": article}
    return HttpResponse(template.render(context, request))

def aboutus(request):
    template = loader.get_template('aboutus/index.html')
    aboutus = Aboutus.objects.all()[0]    
    context = {'aboutus': aboutus}    
    return HttpResponse(template.render(context, request))

def tags(request):
    template = loader.get_template('tags/index.html')
    tags = Tag.objects.all()
    context = {'tags': tags}
    return HttpResponse(template.render(context, request))

def tagDetail(request, tagName=""):
    template = loader.get_template('tags/index.html')
    tags = Tag.objects.all()
    context = {}
    if tagName == "":
        context = {'tags': tags}
    else:
        events = Post.objects.filter(tags__name__in=[tagName], typePost=TYPE_EVENT)        
        locations = Post.objects.filter(tags__name__in=[tagName], typePost=TYPE_LOCATION)
        articles = Post.objects.filter(tags__name__in=[tagName], typePost=TYPE_ARTICLE)
        
        context = {
            'tags': tags,
            'events': events, 
            'locations': locations, 
            'articles': articles
        }
    
    return HttpResponse(template.render(context, request))
