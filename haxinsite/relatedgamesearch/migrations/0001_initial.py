# Generated by Django 2.0.3 on 2018-03-25 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BGGUserFavoriteGames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bgg_user', models.CharField(max_length=200)),
                ('Game1', models.CharField(max_length=200)),
                ('Game2', models.CharField(max_length=200)),
                ('Game3', models.CharField(max_length=200)),
                ('Game4', models.CharField(max_length=200)),
                ('Game5', models.CharField(max_length=200)),
                ('Game6', models.CharField(max_length=200)),
                ('Game7', models.CharField(max_length=200)),
                ('Game8', models.CharField(max_length=200)),
                ('Game9', models.CharField(max_length=200)),
                ('Game10', models.CharField(max_length=200)),
            ],
        ),
    ]
