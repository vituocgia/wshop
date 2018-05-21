# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django
from django.db import migrations, models
from django.utils import version


class Migration(migrations.Migration):
    replaces = [
        ('wshop_testing', '0001_initial'),
        ('wshop_testing', '0002_add_filters'),
        ('wshop_testing', '0003_update_managers'),
    ]

    dependencies = [
        ('wshop', '0001_squashed_0039_alter_names'),
        ('campaigns', '0001_squashed_0011_alter_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarrierWithCheckoutPhase',
            fields=[
                ('customcarrier_ptr', models.OneToOneField(
                    serialize=False,
                    to='wshop.CustomCarrier',
                    primary_key=True,
                    parent_link=True,
                    auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wshop.customcarrier', ),
            managers = (
                [] if version.get_docs_version() == "1.8" else [('_default_manager', django.db.models.manager.Manager())]
            )
        ),
        migrations.CreateModel(
            name='ExpensiveSwedenBehaviorComponent',
            fields=[
                ('servicebehaviorcomponent_ptr', models.OneToOneField(
                    serialize=False,
                    to='wshop.ServiceBehaviorComponent',
                    primary_key=True,
                    parent_link=True,
                    auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wshop.servicebehaviorcomponent', )),
        migrations.CreateModel(
            name='PaymentWithCheckoutPhase',
            fields=[
                ('custompaymentprocessor_ptr', models.OneToOneField(
                    serialize=False,
                    to='wshop.CustomPaymentProcessor',
                    primary_key=True,
                    parent_link=True,
                    auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wshop.custompaymentprocessor', ),
            managers=(
                [] if version.get_docs_version() == "1.8" else [('_default_manager', django.db.models.manager.Manager())]
            )
        ),
        migrations.CreateModel(
            name='PseudoPaymentProcessor',
            fields=[
                ('paymentprocessor_ptr', models.OneToOneField(
                    serialize=False,
                    to='wshop.PaymentProcessor',
                    primary_key=True,
                    parent_link=True,
                    auto_created=True)),
                ('bg_color', models.CharField(
                    blank=True,
                    max_length=20,
                    verbose_name='Payment Page Background Color',
                    default='white')),
                ('fg_color', models.CharField(
                    blank=True,
                    max_length=20,
                    verbose_name='Payment Page Text Color',
                    default='black')),
            ],
            options={
                'abstract': False,
            },
            bases=('wshop.paymentprocessor', ),
            managers=(
                [] if version.get_docs_version() == "1.8" else [('_default_manager', django.db.models.manager.Manager())]
            )
        ),
        migrations.CreateModel(
            name='UltraFilter',
            fields=[
                ('catalogfilter_ptr', models.OneToOneField(
                    serialize=False,
                    to='campaigns.CatalogFilter',
                    primary_key=True,
                    parent_link=True,
                    auto_created=True)),
                ('categories', models.ManyToManyField(
                    to='wshop.Category', related_name='ultrafilter2')),
                ('category', models.ForeignKey(
                    to='wshop.Category', null=True,
                    related_name='ultrafilte5')),
                ('contact', models.ForeignKey(null=True, to='wshop.Contact')),
                ('derp', models.ForeignKey(
                    to='wshop.Category',
                    null=True,
                    related_name='ultrafilte55')),
                ('product', models.ForeignKey(null=True, to='wshop.Product')),
                ('product_type', models.ForeignKey(
                    null=True, to='wshop.ProductType')),
                ('product_types', models.ManyToManyField(
                    to='wshop.ProductType', related_name='ultrafilter3')),
                ('products', models.ManyToManyField(
                    to='wshop.Product', related_name='ultrafilter1')),
                ('shop_product', models.ForeignKey(
                    null=True, to='wshop.ShopProduct')),
                ('shop_products', models.ManyToManyField(
                    to='wshop.ShopProduct', related_name='ultrafilter4')),
            ],
            options={
                'abstract': False,
            },
            bases=('campaigns.catalogfilter', )),
    ]
