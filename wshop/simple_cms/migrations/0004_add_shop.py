# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-01 16:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wshop.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wshop', '0043_order_customer_fields'),
        ('wshop_simple_cms', '0001_squashed_0003_alter_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wshop.Shop', verbose_name='shop'),
        ),
        migrations.AlterField(
            model_name='page',
            name='identifier',
            field=wshop.core.fields.InternalIdentifierField(blank=True, editable=False, max_length=64, null=True, unique=False),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('shop', 'identifier')]),
        ),
        migrations.AlterField(
            model_name='pagetranslation',
            name='url',
            field=models.CharField(blank=True, default=None, help_text='The page url. Choose a descriptive url so that search engines can rank your page higher. Often the best url is simply the page title with spaces replaced with dashes.', max_length=100, null=True, verbose_name='URL'),
        )
    ]