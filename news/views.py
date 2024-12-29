from django.shortcuts import render,redirect
from .models import Articles
from .forms import ArticlesForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def news_home(request):
    news = Articles.objects.order_by("-date")[:3]
    data = {'news':news,
        'title':'Новости'}
    return render(request,'news/news.html',data)

def view_news(request,news_id):
    news = Articles.objects.get(id=news_id)
    data = {'news':news}
    return render(request,"news/news_view.html",data)


def add_news(request):
    error=""
    if request.method =="POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.autor = request.user
            instance.save()
            return redirect('news')
        else:
            error="Форма была неверной"
    form = ArticlesForm()
    data = {'form':form,
            'error':error}
    return render(request,"news/add_news.html",data)
