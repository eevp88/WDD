# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import documentos.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
        ('home', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('orden', models.PositiveIntegerField(default=0)),
                ('descarga', models.PositiveIntegerField(default=0)),
                ('slug', models.CharField(max_length=100, blank=True)),
                ('archivo', models.FileField(upload_to=b'documentos')),
            ],
            options={
                'ordering': ('orden',),
            },
            bases=(documentos.models.SlugMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Carpeta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('curso', models.ForeignKey(to='home.Curso')),
            ],
            options={
            },
            bases=(documentos.models.SlugMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.CharField(max_length=100, blank=True)),
                ('usuario', models.OneToOneField(to='userprofile.UserProfile')),
            ],
            options={
            },
            bases=(documentos.models.SlugMixin, models.Model),
        ),
        migrations.AddField(
            model_name='carpeta',
            name='profesor',
            field=models.ForeignKey(to='documentos.Profesor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='archivo',
            name='curso',
            field=models.ForeignKey(to='documentos.Carpeta'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='archivo',
            name='profesor',
            field=models.ForeignKey(to='documentos.Profesor'),
            preserve_default=True,
        ),
    ]
