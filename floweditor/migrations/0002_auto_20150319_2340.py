# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floweditor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b1if',
            name='path',
            field=models.CharField(default=b'/B1iXcellerator/exec/webdav/com.sap.b1i.vplatform.scenarios.design/', max_length=300),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='b1if',
            name='port',
            field=models.CharField(default=b'8080', max_length=8),
            preserve_default=True,
        ),
    ]
