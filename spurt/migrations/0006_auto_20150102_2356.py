# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spurt', '0005_auto_20150102_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmbedlyResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('response', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='linkpost',
            name='url_published',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
