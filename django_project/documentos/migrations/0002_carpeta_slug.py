# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carpeta',
            name='slug',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
