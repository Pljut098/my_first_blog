# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_catgory'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=mptt.fields.TreeForeignKey(related_name='cat', blank=True, to='blog.Catgory', null=True),
        ),
    ]
