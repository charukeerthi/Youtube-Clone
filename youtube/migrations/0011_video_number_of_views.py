# Generated by Django 2.2.10 on 2020-06-17 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0010_video_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='number_of_views',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
