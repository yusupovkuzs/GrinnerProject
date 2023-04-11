from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница!',
        'values': ['some', 'hello', '123']
    }
    return render(request, 'main/main-page.html', data)

def about(request):
    return render(request, 'main/about.html')

