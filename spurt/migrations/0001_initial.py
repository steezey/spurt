# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('parent', models.ForeignKey(to='spurt.Comment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.CharField(max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LinkPost',
            fields=[
                ('post_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='spurt.Post')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('original_url', models.URLField()),
                ('description', models.TextField()),
                ('provider_name', models.CharField(max_length=255)),
                ('provider_display', models.TextField()),
                ('favicon_url', models.URLField()),
                ('url_title', models.TextField()),
                ('url_description', models.TextField()),
            ],
            options={
            },
            bases=('spurt.post',),
        ),
        migrations.CreateModel(
            name='TextPost',
            fields=[
                ('post_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='spurt.Post')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
            options={
            },
            bases=('spurt.post',),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='spurt.Post'),
            preserve_default=True,
        ),
    ]
