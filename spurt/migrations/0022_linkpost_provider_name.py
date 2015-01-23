# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spurt', '0021_auto_20150122_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkpost',
            name='provider_name',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
