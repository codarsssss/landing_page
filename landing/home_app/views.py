from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import News, Review, Service
from .forms import ConsultationForm


def handle_form(request, form_class):
    form = form_class(request.POST)
    if form.is_valid():
        # asyncio.run(send_telegram_message(f'{form.instance.username}-{form.instance.number}'))
        form.save()
        messages.success(request, "Скоро мы с Вами свяжемся для консультации")
        request.session['username'] = request.POST.get('username')
        return True
    else:
        form = form_class()
        return False


# Главная страница
def index(request):

    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/')

    news = News.published.all() # Все новости, у которых status = Published
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
    news_obj = get_object_or_404(News, slug=slug)

    context = {
        'title': 'Новости',
        'news_obj': news_obj
    }

    return render(request, 'home_app/news_detail.html', context=context)
