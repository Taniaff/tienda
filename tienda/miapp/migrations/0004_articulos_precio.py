# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0003_articulos_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulos',
            name='precio',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
