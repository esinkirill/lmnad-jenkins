# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-05 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmnad', '0003_auto_20170205_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='elibrary',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='\u041f\u0440\u043e\u0444\u0438\u043b\u044c \u043d\u0430 Elibrary'),
        ),
        migrations.AlterField(
            model_name='people',
            name='science_index',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='\u041d\u0430\u0443\u0447\u043d\u044b\u0439 \u0438\u043d\u0434\u0435\u043a\u0441'),
        ),
    ]
