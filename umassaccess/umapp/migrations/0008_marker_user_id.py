# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 21:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('umapp', '0007_marker_marker_type_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='umapp.user'),
        ),
    ]
