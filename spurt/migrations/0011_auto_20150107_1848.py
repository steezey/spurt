# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spurt', '0010_linkpost_url_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embedlyresponse',
            name='url',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='linkpost',
            name='favicon_url',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='linkpost',
            name='original_url',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='linkpost',
            name='url',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
