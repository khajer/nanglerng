from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('home/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def comEssay(request):
    template = loader.get_template('community/essay.html')
    context = {}
    return HttpResponse(template.render(context, request))

def comTimeline(request, eventId=0):
    template = loader.get_template('community/timeline.html')
    context = {}
    return HttpResponse(template.render(context, request))

def comMap(request, mapId=0):
    template = loader.get_template('community/map.html')
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
    context = {}
    return HttpResponse(template.render(context, request))

def tags(request):
    template = loader.get_template('tags/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
