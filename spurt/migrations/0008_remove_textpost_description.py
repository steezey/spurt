# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spurt', '0007_textpost_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textpost',
            name='description',
        ),
    ]
