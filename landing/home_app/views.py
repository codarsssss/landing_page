from django.shortcuts import render
from django.http import Http404
from .models import News, Review, Service


# Главная страница
def index(request):

    news = News.objects.filter(active=True) # Все активные новости
    review = Review.objects.filter(active=True) # Все активные отзывы
    service = Service.objects.filter(active=True) # Все активные услуги

    context = {
        'title': 'Главная страница',
        'Services': service,
        'Reviews': review,
        'News': news
    }

    return render(request, 'home_app/index.html', context=context)



# Детальный взгляд на пост
def news_detail(request, slug):

    # Если пост с таким slug не будет найден => Http404
    try:
        news_obj = News.object.filter(slug=slug)
    except News.DoesNotExist:
        raise Http404('Такой новости нет.')

    context = {
        'title': 'Новости',
        'news_obj': news_obj
    }

    return render(request, 'home_app/news_detail.html', context=context)
