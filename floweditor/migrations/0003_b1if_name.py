# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floweditor', '0002_auto_20150319_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='b1if',
            name='name',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
