# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spurt', '0012_auto_20150107_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkpost',
            name='media',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
