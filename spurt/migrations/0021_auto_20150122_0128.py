# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spurt', '0020_linkpost_scrape_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linkpost',
            old_name='pub_date',
            new_name='scraped_pub_date',
        ),
    ]
