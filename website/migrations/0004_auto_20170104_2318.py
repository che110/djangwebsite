# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-04 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20170104_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='intime',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='sex',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
