# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floweditor', '0004_auto_20150331_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b1file',
            name='account',
            field=models.ForeignKey(to='accounts.Account'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='b1if',
            name='account',
            field=models.ForeignKey(to='accounts.Account'),
            preserve_default=True,
        ),
    ]
