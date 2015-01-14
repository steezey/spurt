# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spurt', '0016_auto_20150114_0538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linkpost',
            name='author',
        ),
        migrations.AddField(
            model_name='linkpost',
            name='authors',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
