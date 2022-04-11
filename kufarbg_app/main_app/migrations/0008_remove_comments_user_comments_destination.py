# Generated by Django 4.0.2 on 2022-04-11 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_remove_comments_user_comments_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.AddField(
            model_name='comments',
            name='destination',
            field=models.ManyToManyField(to='main_app.UserTrips'),
        ),
    ]