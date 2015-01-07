# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spurt', '0009_auto_20150103_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkpost',
            name='url_author',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
