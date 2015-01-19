# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spurt', '0018_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth_code',
            field=models.CharField(max_length=255, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='auth_code_expiry',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
