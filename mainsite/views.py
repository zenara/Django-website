from django.shortcuts import render
from datetime import datetime
from .models import Article

def index(request):
    context = {
        'current_date':datetime.now(),
        'title':'Home'
    }
    return render(request, 'index.html',context)

def about(request):
    context = {
        'current_date':datetime.now(),
        'title':'About'
    }
    return render(request, 'about.html',context)

def news(request):
    populate_db()
    articles = get_articles()

    context = {
        'articles':articles,
        'current_date':datetime.now(),
        'title':'News'
    }
    return render(request, 'news.html',context)

def get_articles():
    result = Article.objects.all()
    return result

def populate_db():
    if Article.objects.count()==0:
        Article(title = 'first item', content = 'This is the first  test content').save()
        Article(title = 'sec item', content = 'This is the second test content').save()
        Article(title = 'third item', content = 'This is the third test content').save()