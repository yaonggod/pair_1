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
    score = request.GET.get('score')
    password = request.GET.get('password')

    Review.objects.create(title=title, content=content, score=score, password=password)
    return redirect('movie:index')
    
# def detail(request, movie_pk, password):
def detail(request, movie_pk):
    review = Review.objects.get(pk=movie_pk)
    # password_confirm = request.GET.get("password_confirm")
    context = {
        'review' : review
    }

    # if password == password_confirm:
    #     return render(request, 'movie/edit.html', context)
    # else:
    #     return redirect("movie:detail", movie_pk)

    return render(request, 'movie/detail.html', context)

def delete(request, movie_pk):
    review = Review.objects.get(pk=movie_pk)
    review.delete()
    
    return redirect('movie:index')


def update(request, movie_pk):
    review = Review.objects.get(pk=movie_pk)
    title = request.GET.get('title')
    content = request.GET.get('content')
    score = request.GET.get('score')
    review.title = title
    review.content = content
    review.score = score
    review.save()
    return redirect('movie:detail', movie_pk)

def edit(request, movie_pk):
    review = Review.objects.get(pk=movie_pk)

    context = {'review' : review}

    return render(request, 'movie/edit.html', context)

def password_confirm(request, movie_pk):
    password = request.GET.get('password_confirm')
    review = Review.objects.get(pk=movie_pk)
    chk = review.password

    if password == chk:
        return redirect('movie:edit', movie_pk)
    else:
        return redirect('movie:detail', movie_pk)

def search_result(request):
    search = request.GET.get('search')
    result = []
    reviews = Review.objects.all()
    for review in reviews:
        if search in review.title or search in review.content:
            result.append(review)
    total = len(result)
    context = {'result' : result, 'total' : total}
    return render(request, 'movie/search_result.html', context)
