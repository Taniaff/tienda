# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_auto_20151112_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulos',
            name='foto',
            field=models.ImageField(default=1, upload_to='miapp/static/media'),
            preserve_default=False,
        ),
    ]
