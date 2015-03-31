# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '__first__'),
        ('floweditor', '0003_b1if_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='b1file',
            name='account',
            field=models.ForeignKey(default=1, to='accounts.BiffyUser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='b1if',
            name='account',
            field=models.ForeignKey(default=1, to='accounts.BiffyUser'),
            preserve_default=False,
        ),
    ]
