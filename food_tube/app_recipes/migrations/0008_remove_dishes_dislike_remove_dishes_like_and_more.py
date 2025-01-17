# Generated by Django 4.2.7 on 2023-11-16 05:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_recipes', '0007_alter_dishes_dislike_alter_dishes_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dishes',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='dishes',
            name='like',
        ),
        migrations.AddField(
            model_name='dishes',
            name='dislike',
            field=models.ManyToManyField(related_name='dislikes', to=settings.AUTH_USER_MODEL, verbose_name='Дизлайки'),
        ),
        migrations.AddField(
            model_name='dishes',
            name='like',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='Лайки'),
        ),
    ]
