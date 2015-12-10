# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0004_articulos_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='articulos',
            field=models.ForeignKey(to='miapp.articulos', null=True),
        ),
    ]
