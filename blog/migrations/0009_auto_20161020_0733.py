# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20161020_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(null=True, verbose_name='date', auto_now=True),
        ),
    ]
