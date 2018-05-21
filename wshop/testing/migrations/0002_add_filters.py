# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0003_category_products'),
        ('wshop', '0004_update_orderline_refunds'),
        ('wshop_testing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UltraFilter',
            fields=[
                ('catalogfilter_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='campaigns.CatalogFilter')),
                ('categories', models.ManyToManyField(related_name='ultrafilter2', to='wshop.Category')),
                ('category', models.ForeignKey(related_name='ultrafilte5', to='wshop.Category', null=True)),
                ('contact', models.ForeignKey(to='wshop.Contact', null=True)),
                ('derp', models.ForeignKey(related_name='ultrafilte55', to='wshop.Category', null=True)),
                ('product', models.ForeignKey(to='wshop.Product', null=True)),
                ('product_type', models.ForeignKey(to='wshop.ProductType', null=True)),
                ('product_types', models.ManyToManyField(related_name='ultrafilter3', to='wshop.ProductType')),
                ('products', models.ManyToManyField(related_name='ultrafilter1', to='wshop.Product')),
                ('shop_product', models.ForeignKey(to='wshop.ShopProduct', null=True)),
                ('shop_products', models.ManyToManyField(related_name='ultrafilter4', to='wshop.ShopProduct')),
            ],
            options={
                'abstract': False,
            },
            bases=('campaigns.catalogfilter',),
        ),
    ]
