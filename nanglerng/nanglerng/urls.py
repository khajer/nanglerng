"""nanglerng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('community/essay', views.comEssay, name='comEssay'),
    path('community/timeline', views.comTimeline, name='comTimeline'),
    path('community/timeline/<int:eventId>', views.comTimeline, name='comTimeline'),
    path('community/map', views.comMap, name='comMap'),    
    path('community/map/<int:locId>', views.comMapLoc, name='comMap'),    
    path('whatson', views.whatsOn, name='whatson'),
    path('article', views.article, name='article'),
    path('article/<int:articleId>', views.articleDetail, name='articleDetail'),
    path('aboutus', views.aboutus, name='about'),
    path('tags', views.tags, name='tags'),
    path('tags/<str:tagName>', views.tagDetail, name='tagDetail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
