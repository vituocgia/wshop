# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarrierWithCheckoutPhase',
            fields=[
                ('customcarrier_ptr', models.OneToOneField(to='wshop.CustomCarrier', parent_link=True, serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wshop.customcarrier',),
        ),
        migrations.CreateModel(
            name='ExpensiveSwedenBehaviorComponent',
            fields=[
                ('servicebehaviorcomponent_ptr', models.OneToOneField(to='wshop.ServiceBehaviorComponent', parent_link=True, serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wshop.servicebehaviorcomponent',),
        ),
        migrations.CreateModel(
            name='PaymentWithCheckoutPhase',
            fields=[
                ('custompaymentprocessor_ptr', models.OneToOneField(to='wshop.CustomPaymentProcessor', parent_link=True, serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wshop.custompaymentprocessor',),
        ),
        migrations.CreateModel(
            name='PseudoPaymentProcessor',
            fields=[
                ('paymentprocessor_ptr', models.OneToOneField(to='wshop.PaymentProcessor', parent_link=True, serialize=False, auto_created=True, primary_key=True)),
                ('bg_color', models.CharField(verbose_name='Payment Page Background Color', max_length=20, blank=True, default='white')),
                ('fg_color', models.CharField(verbose_name='Payment Page Text Color', max_length=20, blank=True, default='black')),
            ],
            options={
                'abstract': False,
            },
            bases=('wshop.paymentprocessor',),
        ),
    ]
