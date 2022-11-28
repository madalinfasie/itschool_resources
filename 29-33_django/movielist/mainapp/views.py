from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, FormView, CreateView, DeleteView, UpdateView

from mainapp import models, forms


class HomepageView(ListView):
    model = models.Movie
    template_name = 'mainapp/home.html'
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra_arg'] = 'Paco'
        return context


class MovieView(DetailView):
    model = models.Movie
    template_name = 'mainapp/details.html'
    context_object_name = 'movie'


class ContactFormView(CreateView):
    template_name = 'mainapp/add.html'
    form_class = forms.MovieForm
    model = models.Movie
    success_url = '/'

def homepage(request):
    title = request.GET.get('title')
    if title:
        movies = models.Movie.objects.filter(title__contains=title)
    else:
        movies = models.Movie.objects.all()

    return render(request, 'mainapp/home.html', {'movies': movies})


def details(request, id):
    return render(request, 'mainapp/details.html', {'movie': models.Movie.objects.get(id=id)})

def add(request):
    if request.method == 'POST':
        form = forms.MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = forms.MovieForm()

    return render(request, 'mainapp/add.html', {'form': form})



def create_titles(request):
    models.Movie.objects.create(title='Plansul leilor', description='e misto, l-am inventat', release_date=datetime(2014, 1, 23))
    models.Movie.objects.create(title='Harcea parcea', description='decent', release_date=datetime(2011, 12, 3))
    models.Movie.objects.create(title='Micul print', description='de copii si adulti', release_date=datetime(2016, 5, 26))
    models.Movie.objects.create(title='M-am sculat de dimineata', description='ia ghici', release_date=datetime(2022, 11, 23))