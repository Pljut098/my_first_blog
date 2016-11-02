# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import mptt.fields
import ckeditor.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Category', max_length=150)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(to='blog.Category', blank=True, related_name='children', verbose_name='Parrent class', null=True)),
            ],
            options={
                'db_table': 'category',
                'verbose_name': 'Category',
                'ordering': ('tree_id', 'level'),
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('comments_text', models.TextField()),
                ('comments_date', models.DateTimeField(verbose_name='date', auto_now=True, null=True)),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Теги', unique=True, max_length=50)),
            ],
            options={
                'db_table': 'keywords',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('text', ckeditor.fields.RichTextField()),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('image', models.ImageField(verbose_name='image', blank=True, upload_to='image/', null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('category', mptt.fields.TreeForeignKey(to='blog.Category', blank=True, null=True, related_name='cat')),
                ('keywords', models.ManyToManyField(related_name='keywords', verbose_name='Теги', to='blog.Keywords', related_query_name='keyword')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_article_id',
            field=models.ForeignKey(to='blog.Post'),
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
