# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-14 23:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wshop', '0022_add_favicon'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='visible_in_menu',
            field=models.BooleanField(default=True),
        ),
    ]
