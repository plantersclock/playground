import sqlite3

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.views import generic
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.db.models import Count
from collections import Counter


from .forms import FavoriteGameForm
from .models import BGGUser, BGGGame, UserGameRanking


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
            favgameuserlist = []
            favgameuserlist = UserGameRanking.objects.filter(game_name__name = favgamename)
            favgameuserlist = [p.user_name.name for p in favgameuserlist]
            print(favgameuserlist)
            otherfavgames = [x.game_name.name for x in UserGameRanking.objects.filter(user_name__name__in = favgameuserlist)]
            otherfavgames = (Counter(otherfavgames)).most_common()[1:11]
            otherfavgames = (str(item[0]) + ': ' + str(item[1]) for item in otherfavgames)
            print(otherfavgames)
                 
            
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'relatedgamesearch/favoritegame.html', {'form': form, 'otherfavgames': otherfavgames})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FavoriteGameForm()

    return render(request, 'relatedgamesearch/favoritegame.html', {'form': form})