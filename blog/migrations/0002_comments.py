# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('comments_text', models.TextField()),
                ('comments_article', models.ForeignKey(to='blog.Post')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]
