# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models

import wshop.core.fields
import wshop.front.models.stored_basket
import wshop.utils.properties


class Migration(migrations.Migration):
    replaces = [
        ('wshop_front', '0001_initial'),
        ('wshop_front', '0002_stored_basket_model_name_translatable'),
    ]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wshop', '0001_squashed_0039_alter_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoredBasket',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    verbose_name='ID',
                    serialize=False,
                    primary_key=True)),
                ('key', models.CharField(
                    verbose_name='key',
                    default=wshop.front.models.stored_basket.generate_key,
                    max_length=32)),
                ('created_on', models.DateTimeField(
                    verbose_name='created on',
                    db_index=True,
                    auto_now_add=True)),
                ('updated_on', models.DateTimeField(
                    verbose_name='updated on', db_index=True, auto_now=True)),
                ('persistent', models.BooleanField(
                    verbose_name='persistent', db_index=True, default=False)),
                ('deleted', models.BooleanField(
                    verbose_name='deleted', db_index=True, default=False)),
                ('finished', models.BooleanField(
                    verbose_name='finished', db_index=True, default=False)),
                ('title', models.CharField(
                    verbose_name='title', max_length=64, blank=True)),
                ('data', wshop.core.fields.TaggedJSONField(
                    verbose_name='data')),
                ('taxless_total_price_value',
                 wshop.core.fields.MoneyValueField(
                     decimal_places=9,
                     max_digits=36,
                     verbose_name='taxless total price',
                     default=0,
                     blank=True,
                     null=True)),
                ('taxful_total_price_value', wshop.core.fields.MoneyValueField(
                    decimal_places=9,
                    max_digits=36,
                    verbose_name='taxful total price',
                    default=0,
                    blank=True,
                    null=True)),
                ('currency', wshop.core.fields.CurrencyField(
                    verbose_name='currency', max_length=4)),
                ('prices_include_tax', models.BooleanField(
                    verbose_name='prices include tax')),
                ('product_count', models.IntegerField(
                    verbose_name='product_count', default=0)),
                ('creator', models.ForeignKey(
                    to=settings.AUTH_USER_MODEL,
                    verbose_name='creator',
                    related_name='baskets_created',
                    blank=True,
                    null=True)),
                ('customer', models.ForeignKey(
                    to='wshop.Contact',
                    verbose_name='customer',
                    related_name='customer_baskets',
                    blank=True,
                    null=True)),
                ('orderer', models.ForeignKey(
                    to='wshop.PersonContact',
                    verbose_name='orderer',
                    related_name='orderer_baskets',
                    blank=True,
                    null=True)),
                ('products', models.ManyToManyField(
                    verbose_name='products', blank=True, to='wshop.Product')),
                ('shop', models.ForeignKey(
                    verbose_name='shop', to='wshop.Shop')),
            ],
            bases=(wshop.utils.properties.MoneyPropped, models.Model), ),
        migrations.AlterModelOptions(
            name='storedbasket',
            options={
                'verbose_name_plural': 'stored baskets',
                'verbose_name': 'stored basket'
            }, ),
    ]
