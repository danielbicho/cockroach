# Generated by Django 2.0.7 on 2018-07-15 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0007_game_game_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamematch',
            name='match_points',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamematch',
            name='match_player_standing',
            field=models.IntegerField(),
        ),
    ]
