# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 21:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('umapp', '0006_marker_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='marker_type_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='umapp.marker_type'),
        ),
    ]
