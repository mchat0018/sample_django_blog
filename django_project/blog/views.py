from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author':'MihirC',
        'title': 'Blog Post 1',
        'content':'First Post Content',
        'date_posted': 'December 24, 2021'
    },
    {
        'author':'Jane Doe',
        'title': 'Blog Post 2',
        'content':'Second Post Content',
        'date_posted': 'December 25, 2021'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})