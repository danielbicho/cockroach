# Generated by Django 2.0.7 on 2018-07-15 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='player_nickname',
            field=models.CharField(default='dbicho', max_length=15, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='player_name',
            field=models.TextField(),
        ),
    ]
