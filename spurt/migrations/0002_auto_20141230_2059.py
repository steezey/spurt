# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spurt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkpost',
            name='favicon_url',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='linkpost',
            name='provider_display',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='linkpost',
            name='url_description',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
