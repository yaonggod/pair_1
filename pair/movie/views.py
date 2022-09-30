from django.shortcuts import render, redirect 
from .models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    total = Review.objects.all().count()
    context = {
        'reviews': reviews,
        'total' : total,
    }
    return render(request, 'movie/index.html', context)

def new(request):
    return render(request, 'movie/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    Review.objects.create(title=title, content=content)
    return redirect('movie:index')
    
def detail(request, movie_pk):
    review = Review.objects.get(pk=movie_pk)
    context = {
        'review' : review
    }
    return render(request, 'movie/detail.html', context)

def delete(request, movie_pk):
    review = Review.objects.get(pk=movie_pk)
    review.delete()
    
    return redirect('movie:index')


def update(request, movie_pk):
    review = Review.objects.get(pk=movie_pk)
    title = request.GET.get('title')
    content = request.GET.get('content')
    review.title = title
    review.content = content
    review.save()
    return redirect('movie:detail', movie_pk)

def edit(request, movie_pk):
    review = Review.objects.get(pk=movie_pk)
    context = {'review' : review}
    return render(request, 'movie/edit.html', context)