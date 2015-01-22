# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spurt', '0019_auto_20150118_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkpost',
            name='scrape_token',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
