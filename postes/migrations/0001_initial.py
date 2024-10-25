# Generated by Django 5.1.1 on 2024-09-21 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=1000)),
                ('slug', models.SlugField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),                      
    ]
        