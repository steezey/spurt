# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('authorUDID', models.CharField(max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=False)),
                ('url', models.URLField()),
                ('original_url', models.URLField()),
                ('content', models.TextField()),
                ('description', models.TextField()),
                ('provider_name', models.CharField(max_length=255)),
                ('provider_display', models.TextField()),
                ('favicon_url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
