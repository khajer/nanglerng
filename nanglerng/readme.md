django-admin startproject nanglerng

python3 manage.py migrate

# install font awesome
pip3 install -r requirements.txt

# run server
python3 manage.py runserver
python3 manage.py runserver 8080

# create model
python3 manage.py startapp polls


# migrate database
python3 manage.py makemigrations nanglerng      // (Create the migrations)
python3 manage.py migrate nanglerng             // (execute the SQL commands). 

# query 
python3 manage.py shell
`
from nanglerng.models import Post
Post.objects.all()
Post.objects.all().filter(mainFlag=True)
`

# admin 
python3 manage.py createsuperuser
admin
nanglerng0222


# quill
//pip install django-quill-editor
settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    ...
    'django_quill',
]


# taggit
//pip install taggit
from taggit.models import Tag
tags = Tag.objects.all()


from nanglerng.models import Post
posts = Post.objects.filter(tags__name__in=["tagName"])
posts = Post.objects.filter(typePost="1")

# migrate database
python3 manage.py makemigrations nanglerng      // (Create the migrations)
python3 manage.py migrate nanglerng             // (execute the SQL commands). 
