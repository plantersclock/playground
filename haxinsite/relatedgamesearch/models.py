from django.db import models

# Create your models here.

class BGGUser(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class BGGGame(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class UserGameRanking(models.Model):
    user_name = models.ForeignKey(BGGUser, on_delete=models.CASCADE)
    game_name = models.ForeignKey(BGGGame, on_delete=models.CASCADE)
    rating = models.FloatField(max_length=10, default=9)
    
    def __str__(self):
        template = '{0.user_name} {0.game_name} {0.rating}'
        return template.format(self)




