from django import forms

class FavoriteGameForm(forms.Form):
    favorite_game_name = forms.CharField(label='What is your favorite game?', max_length=100)