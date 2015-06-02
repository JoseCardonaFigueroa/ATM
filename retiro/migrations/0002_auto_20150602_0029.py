# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retiro', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retiros',
            name='user',
        ),
        migrations.RemoveField(
            model_name='cuenta',
            name='cantidad_total',
        ),
        migrations.DeleteModel(
            name='Retiros',
        ),
    ]
