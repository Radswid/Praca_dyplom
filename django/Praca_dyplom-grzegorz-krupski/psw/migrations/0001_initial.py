# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50, verbose_name='IP')),
                ('system', models.CharField(max_length=50, verbose_name='System')),
                ('ram', models.IntegerField(verbose_name='Ram')),
                ('quote', models.IntegerField(verbose_name='Quote')),
            ],
            options={
                'verbose_name_plural': 'Komendy',
                'verbose_name': 'Komenda',
            },
        ),
    ]
