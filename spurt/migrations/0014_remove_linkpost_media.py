# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spurt', '0013_linkpost_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linkpost',
            name='media',
        ),
    ]
