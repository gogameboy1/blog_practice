# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from blog_site.models import Article
from django.http import HttpResponseRedirect
from django import forms


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'content']

# Create your views here.
def index(request):
    posts = Article.objects.all()
    return render(request, 'blog_site/index.html', {'posts' : posts})

def addArticle(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            new_article = form.save()
            return HttpResponseRedirect('/')

    form = ArticleForm()
    return render(request, 'addArticle.html', {'form': form})

def editArticle(request, title):
    query_article = Article.objects.get(title=title)
    if request.method == 'POST':
        mod_article = ArticleForm(request.POST, instance=query_article)

        if mod_article.is_valid:
            mod_article.save()
            return HttpResponseRedirect('/')
    mod_article = ArticleForm(instance=query_article)
    return render(request, 'editArticle.html', {'form': mod_article})

def showCat(request, category):
    posts = Article.objects.filter(category=category)
    return render(request, 'blog_site/showCat.html', {'posts': posts})
