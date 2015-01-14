# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spurt', '0014_remove_linkpost_media'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linkpost',
            old_name='url_author',
            new_name='scraped_author',
        ),
        migrations.RenameField(
            model_name='linkpost',
            old_name='url_content',
            new_name='scraped_content',
        ),
        migrations.RenameField(
            model_name='linkpost',
            old_name='url_content_filtered',
            new_name='scraped_content_filtered',
        ),
        migrations.RenameField(
            model_name='linkpost',
            old_name='url_description',
            new_name='scraped_description',
        ),
        migrations.RenameField(
            model_name='linkpost',
            old_name='url_published',
            new_name='scraped_published',
        ),
        migrations.RenameField(
            model_name='linkpost',
            old_name='url_title',
            new_name='scraped_title',
        ),
    ]
