# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spurt', '0004_post_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkpost',
            name='kind',
            field=models.CharField(default=b'link', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='textpost',
            name='kind',
            field=models.CharField(default=b'text', max_length=255),
            preserve_default=True,
        ),
    ]
