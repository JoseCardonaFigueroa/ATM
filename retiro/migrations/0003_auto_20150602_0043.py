# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retiro', '0002_auto_20150602_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuenta',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cuenta',
        ),
    ]
