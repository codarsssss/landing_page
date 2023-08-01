from django.shortcuts import render

# Create your views here.


def index(request):

    context = {
        'title': 'Hello, World!'
    }

    return render(request, 'home_app/index.html', context=context)