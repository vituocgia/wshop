# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wshop.utils.properties
import wshop.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CgpPrice',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('price_value', wshop.core.fields.MoneyValueField(verbose_name='price', decimal_places=9, max_digits=36)),
                ('group', models.ForeignKey(verbose_name='contact group', to='wshop.ContactGroup')),
                ('product', models.ForeignKey(related_name='+', to='wshop.Product', verbose_name='product')),
                ('shop', models.ForeignKey(verbose_name='shop', to='wshop.Shop')),
            ],
            options={
                'verbose_name': 'product price',
                'verbose_name_plural': 'product prices',
            },
            bases=(wshop.utils.properties.MoneyPropped, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='cgpprice',
            unique_together=set([('product', 'shop', 'group')]),
        ),
    ]
