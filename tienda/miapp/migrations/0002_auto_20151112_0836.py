# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentarios',
            old_name='tema',
            new_name='comentario',
        ),
    ]
