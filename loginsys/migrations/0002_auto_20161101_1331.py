# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(default='image/None/no-img.jpg', blank=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
