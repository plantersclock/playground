from django.db import models

# Create your models here.

class BGGUser(models.Model):
    bgg_user = models.CharField(max_length=200)

    def __str__(self):
        return self.bgg_user

class BGGGame(models.Model):
    bgg_game = models.CharField(max_length=200)

    def __str__(self):
        return self.bgg_game

class Rank(models.Model):
    rank = models.CharField(max_length=200)

    def __str__(self):
        return self.rank

class UserGameRanking(models.Model):
    bgg_user = models.ForeignKey(BGGUser, on_delete=models.CASCADE)
    bgg_game = models.ForeignKey(BGGGame, on_delete=models.CASCADE)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)




