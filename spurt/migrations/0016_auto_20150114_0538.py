# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spurt', '0015_auto_20150111_0041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linkpost',
            old_name='scraped_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='linkpost',
            old_name='scraped_content',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='linkpost',
            name='favicon_url',
        ),
        migrations.RemoveField(
            model_name='linkpost',
            name='provider_display',
        ),
        migrations.RemoveField(
            model_name='linkpost',
            name='provider_name',
        ),
        migrations.RemoveField(
            model_name='linkpost',
            name='scraped_content_filtered',
        ),
        migrations.RemoveField(
            model_name='linkpost',
            name='scraped_description',
        ),
        migrations.RemoveField(
            model_name='linkpost',
            name='scraped_published',
        ),
        migrations.AddField(
            model_name='linkpost',
            name='author_name',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='linkpost',
            name='dek',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='linkpost',
            name='domain',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='linkpost',
            name='embedly_safe',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='linkpost',
            name='favicon',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='linkpost',
            name='lead',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='linkpost',
            name='lead_image',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='linkpost',
            name='pub_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='linkpost',
            name='rddme_url',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='linkpost',
            name='description',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
