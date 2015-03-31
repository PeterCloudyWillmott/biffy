# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floweditor', '0005_auto_20150331_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b1if',
            name='password',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='b1if',
            name='user',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
