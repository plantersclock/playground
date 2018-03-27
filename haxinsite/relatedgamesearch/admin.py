from django.contrib import admin

# Register your models here.
from .models import BGGUser, BGGGame, UserGameRanking

admin.site.register(BGGUser)
admin.site.register(BGGGame)
admin.site.register(UserGameRanking)