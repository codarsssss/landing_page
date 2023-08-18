from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Review, Service
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

    review = Review.objects.filter(active=True) # Все активные отзывы
    service = Service.objects.filter(active=True) # Все активные услуги

    context = {
        'title': 'Главная страница',
        'Services': service,
        'Reviews': review,
        'achievements': range(8)
    }

    return render(request, 'home_app/index.html', context=context)
