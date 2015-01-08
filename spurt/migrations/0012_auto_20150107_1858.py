# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spurt', '0011_auto_20150107_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkpost',
            name='provider_name',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='linkpost',
            name='url_title',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
