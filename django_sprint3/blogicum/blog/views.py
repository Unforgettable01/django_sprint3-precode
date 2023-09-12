from django.shortcuts import render
from django.http import Http404 


def index(request):
    context = {'list_posts' : posts}
    template = 'blog/index.html'
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    try: 
        post = posts[id] 
    except IndexError as exc: 
        raise Http404('Блог не найден') from exc 
    context = {'post': post} 
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category' : category_slug }
    return render(request, template, context)