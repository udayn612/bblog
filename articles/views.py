from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def article_list(request):
    articles=Article.objects.all().order_by('date')
    return render(request,'articles/article_list.html',{'articles':articles})
