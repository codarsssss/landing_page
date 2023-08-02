from django.shortcuts import render
from django.http import Http404
from .models import News, Review


# Главная страница
def index(request):

    news = News.objects.filter(active=True)
    review = Review.objects.filter(active=True)

    context = {
        'title': 'Главная страница',
        'Review': review,
        'News': news
    }

    return render(request, 'home_app/index.html', context=context)



# Детальный взгляд на пост
def news_detail(request, slug):

    try:
        news_obj = News.object.filter(slug=slug)
    except News.DoesNotExist:
        raise Http404('Такой новости нет.')

    context = {
        'title': 'Новости',
        'news_obj': news_obj
    }

    return render(request, 'home_app/news_detail.html', context=context)
