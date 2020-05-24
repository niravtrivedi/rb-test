# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-05-24 07:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiv1', '0003_auto_20200524_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submittedexam',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submittedexam', to='apiv1.Questions'),
        ),
    ]