# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-29 21:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wshop', '0034_shops_for_supplier'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name': 'shop', 'verbose_name_plural': 'shops'},
        ),
    ]