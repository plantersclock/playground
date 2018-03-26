# Generated by Django 2.0.3 on 2018-03-25 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relatedgamesearch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BGGGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bgg_game', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BGGUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bgg_user', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rank', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserGameRanking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bgg_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relatedgamesearch.BGGGame')),
                ('bgg_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relatedgamesearch.BGGUser')),
                ('rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relatedgamesearch.Rank')),
            ],
        ),
        migrations.DeleteModel(
            name='BGGUserFavoriteGames',
        ),
    ]
