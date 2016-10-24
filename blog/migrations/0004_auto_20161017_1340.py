# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='comments_article',
            new_name='comments_article_id',
        ),
    ]
