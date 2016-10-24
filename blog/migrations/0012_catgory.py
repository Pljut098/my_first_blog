# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20161021_0623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catgory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=150, verbose_name='Category')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(null=True, to='blog.Catgory', related_name='children', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Category',
                'db_table': 'category',
                'verbose_name': 'Category',
            },
        ),
    ]
