# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0005_auto_20151210_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='usuario',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
