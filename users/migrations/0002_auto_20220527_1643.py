# Generated by Django 2.1 on 2022-05-27 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default="Hello! I'm a user of the blog.", max_length=3000),
        ),
    ]
