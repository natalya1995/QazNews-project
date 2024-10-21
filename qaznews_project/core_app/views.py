from django.shortcuts import render, get_object_or_404, redirect
from .models import Tag, Post
from django.core.paginator import Paginator
from django.db.models import Q

def home_page(request):
    primary_posts=Post.objects.all().order_by('-created_at')[:1]
    last_posts=Post.objects.all().order_by('-created_at')[:6]
    tags=Tag.objects.all()[:3]
    context={
       'primary_posts':primary_posts,
        'last_posts':last_posts,
        'tags':tags
    }
    return render(request,"./client/home.html",context)
def all_news_page(request):
    tags=Tag.objects.all()
    post_list=Post.objects.all().order_by('-created_at')
    paginator=Paginator(post_list,5)
    page_number=request.GET.get('page')
    posts=paginator.get_page(page_number)
    context={
        'tags':tags,
        'posts':posts
    }
    return render(request,"./client/all-news.html",context)

def news_detail_page(request,pk):
    post=get_object_or_404(Post,pk=pk)
    tags=Tag.objects.all()
    last_posts=Post.objects.all().order_by('-created_at')[:3]
    context={
        'post':post,
        'tags':tags,
        'last_posts':last_posts
    }
    return render(request,"./client/news-detail.html",context)

def search_page(request):
     tags=Tag.objects.all()
     context={
        'tags':tags
     }
     return render(request,"./client/search.html",context)

def search_results_page(request):
    query=request.GET.get('q','').strip()
    post_list=Post.objects.filter(
        Q(title__icontains=query)
    )|Post.objects.filter(
                Q(description__icontains=query)
    )
    paginator=Paginator(post_list,5)
    page_number=request.GET.get('page')
    posts=paginator.get_page(page_number)
    tags=Tag.objects.all()
    context={
        'tags':tags,
        'posts':posts,
        'query':query
    }
    return render(request,"./client/search-results.html",context)

def tags_news_page(request,slug):
    tag=get_object_or_404(Tag,slug=slug)
    post_list=Post.objects.filter(tag=tag)
    paginator=Paginator(post_list,5)
    page_number=request.GET.get('page')
    posts=paginator.get_page(page_number)
    tags=Tag.objects.all()
    context={
        'tag':tag,
        'posts':posts,
        'tags':tags
    }
    return render(request,"./client/tags-news.html",context)