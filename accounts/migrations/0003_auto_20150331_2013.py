# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150331_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biffyuser',
            name='user',
            field=models.OneToOneField(related_name='biffyuser', null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
