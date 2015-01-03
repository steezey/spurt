# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spurt', '0008_remove_textpost_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkpost',
            name='url_content',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='linkpost',
            name='url_content_filtered',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
