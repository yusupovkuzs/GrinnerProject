from django.shortcuts import render, redirect
from .models import users
from .forms import usersFormRegistrationStudent
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = users.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

def sign(request):
    return render(request, 'news/sign.html')

def create(request):
    return render(request, 'news/create.html')

def teacher(request):
    return render(request, 'news/teacher.html')

class NewsDetailView(DetailView):
    model = users
    template_name = 'news/news_detail.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = users
    template_name = 'news/create.html'
    form_class = usersFormRegistrationStudent

class NewsDeleteView(DeleteView):
    model = users
    template_name = 'news/news_delete.html'
    success_url = '/news/'


def student(request):
    error=''
    if request.method == "POST":
        form = usersFormRegistrationStudent(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма была неверной'

    form = usersFormRegistrationStudent()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/student.html', data)
