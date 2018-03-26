from django.contrib import admin

# Register your models here.
from .models import BGGUser, BGGGame, Rank, UserGameRanking

admin.site.register(BGGUser)
admin.site.register(BGGGame)
admin.site.register(Rank)
admin.site.register(UserGameRanking)