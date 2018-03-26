from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.views import generic
from django.http import HttpResponseRedirect
from django.http import HttpRequest


from .forms import FavoriteGameForm


# Create your views here.


def index(request):
    return HttpResponse("SEARCH ME")

def get_favorite_game_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FavoriteGameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            favgamename = form.cleaned_data['favorite_game_name']
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'relatedgamesearch/favoritegame.html', {'form': form, 'favgamename': favgamename})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FavoriteGameForm()

    return render(request, 'relatedgamesearch/favoritegame.html', {'form': form})