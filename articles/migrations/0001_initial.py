# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='заголовок')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='посилання')),
                ('excerpt', models.TextField(verbose_name='коротикий зміст статті')),
                ('article', models.TextField(verbose_name='повний зміст статті')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('publish', models.BooleanField(default=True, verbose_name='опублікована')),
            ],
            options={
                'verbose_name_plural': 'статті блогу',
                'verbose_name': 'статтю блогу',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Тег')),
            ],
            options={
                'verbose_name_plural': 'теги',
                'verbose_name': 'тег',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='articles.Tag', verbose_name='теги'),
        ),
    ]
