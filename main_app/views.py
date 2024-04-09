from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movie, Show



# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
   return render(request, 'about.html')

def shows_index(request):
   return render(request, 'all_tv_shows.html')

def movies_index(request):
   return render(request, 'all_movies.html')

def party_index(request):
   movies = Movie.objects.all()
   shows = Show.objects.all()
   return render(request, 'party/index.html', {
      'movies': movies,
      'shows': shows
   })

def my_profile(request):
   return render(request, 'my_profile.html')


class MovieCreate(CreateView):
    model = Movie

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class ShowCreate(CreateView):
    model = Show

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    # replace '/' with /index
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
