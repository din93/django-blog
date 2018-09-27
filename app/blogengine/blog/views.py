from django.shortcuts import render

# Create your views here.

def posts_list(request):
    posts = ['post1', 'post2', 'post3', 'post']
    return render(request, 'blog/index.html', context={'posts': posts})