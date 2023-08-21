import asyncio
from django.shortcuts import render, redirect
from .forms import ConsultationForm
from .notification_bot import send_telegram_message


def handle_form(request, form_class):
    form = form_class(request.POST)
    if form.is_valid():
        asyncio.run(send_telegram_message(f'{form.instance.username}\n{form.instance.number}'))
        form.save()
        return True
    else:
        form = form_class()
        return False


# Главная страница
def index(request):

    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/')

    context = {
        'title': 'Главная страница'
    }

    return render(request, 'home_app/index.html', context=context)


def policy_view(request):
    if request.method == 'POST':
        if handle_form(request, ConsultationForm):
            return redirect('/')

    return render(request, 'home_app/policy.html', context={'title': 'Политика конфиденциальности'})
