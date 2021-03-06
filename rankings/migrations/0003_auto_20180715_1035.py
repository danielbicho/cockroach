# Generated by Django 2.0.7 on 2018-07-15 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0002_auto_20180715_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='player_name',
        ),
        migrations.AddField(
            model_name='player',
            name='player_first_name',
            field=models.CharField(default='Daniel', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='player_last_name',
            field=models.CharField(default='Bicho', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='player_photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
