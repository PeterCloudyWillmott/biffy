# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='B1file',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contents', models.TextField()),
                ('dirty', models.BooleanField(default=False)),
                ('flow', models.CharField(max_length=200)),
                ('filename', models.CharField(max_length=200)),
                ('path', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='B1if',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=300)),
                ('port', models.CharField(max_length=8)),
                ('user', models.CharField(max_length=24)),
                ('password', models.CharField(max_length=24)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
