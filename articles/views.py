from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth.decorators import login_required
# Create your views here.

def article(request):
    # get the first five articles
    count = Article.objects.count()
    articles = Article.objects.order_by('date')[count-5:count]
    new_articles = []
    for article in articles:
        new_articles.insert(0,article)
    return render(request,'article.html',context={'articles':new_articles})

def article_detail(request, id):
    article = Article.objects.get(id=int(id))
    context = {
        'title':article.title,
        'content':article.content,
        'writer':article.writer,
        'date': article.date
    }
    return render(request,'article_detail.html',context=context)

@login_required
def write_article(request):
    if request.method == 'POST':
        content = request.POST["article_content"]
        title = request.POST["title"]
        if not content or not title:
            return HttpResponse('Fill all the required fields')
        user = User.objects.get(username=request.user.username)
        article = Article(title=title,content=content,writer=user,date=date.today())
        article.save()
        return redirect('article')
    context = {
        'sub_heading': '<h2>{ Your Heading }</h2>',
        'img':'<img src="{ Your image url }" alt="{ details of your image }" width="{ width of your image }">' ,
        'content': '<p> { your content } </p>'
    }
    return render(request,'write_article.html',context=context)
