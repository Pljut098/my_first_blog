# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_post_dislikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comments_author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_date',
            field=models.DateField(auto_now=True, verbose_name='date', null=True),
        ),
    ]
