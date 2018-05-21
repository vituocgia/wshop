# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-02-21 06:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wshop.core.fields
import wshop.utils.properties


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0008_freeproductline_quantity_to_quantityfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketTotalUndiscountedProductAmountCondition',
            fields=[
                ('basketcondition_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='campaigns.BasketCondition')),
                ('amount_value', wshop.core.fields.MoneyValueField(blank=True, decimal_places=9, default=None, max_digits=36, null=True, verbose_name='basket total amount')),
            ],
            options={
                'abstract': False,
            },
            bases=(wshop.utils.properties.MoneyPropped, 'campaigns.basketcondition'),
        ),
        migrations.CreateModel(
            name='DiscountPercentageFromUndiscounted',
            fields=[
                ('basketdiscounteffect_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='campaigns.BasketDiscountEffect')),
                ('discount_percentage', models.DecimalField(blank=True, decimal_places=5, help_text='The discount percentage for this campaign.', max_digits=6, null=True, verbose_name='discount percentage')),
            ],
            options={
                'abstract': False,
            },
            bases=('campaigns.basketdiscounteffect',),
        ),
        migrations.AlterField(
            model_name='basketcampaign',
            name='active',
            field=models.BooleanField(default=False, help_text='Check this if the campaign is currently active. Please also set a start and end date.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='basketcampaign',
            name='end_datetime',
            field=models.DateTimeField(blank=True, help_text='The date and time the campaign ends. This is only applicable if the campaign is marked as active.', null=True, verbose_name='end date and time'),
        ),
        migrations.AlterField(
            model_name='basketcampaign',
            name='shop',
            field=models.ForeignKey(help_text='The shop where the campaign is active.', on_delete=django.db.models.deletion.CASCADE, to='wshop.Shop', verbose_name='shop'),
        ),
        migrations.AlterField(
            model_name='basketcampaign',
            name='start_datetime',
            field=models.DateTimeField(blank=True, help_text='The date and time the campaign starts. This is only applicable if the campaign is marked as active.', null=True, verbose_name='start date and time'),
        ),
        migrations.AlterField(
            model_name='basketcampaigntranslation',
            name='public_name',
            field=models.CharField(help_text='The campaign name to show in the store front.', max_length=120, verbose_name='public name'),
        ),
        migrations.AlterField(
            model_name='catalogcampaign',
            name='active',
            field=models.BooleanField(default=False, help_text='Check this if the campaign is currently active. Please also set a start and end date.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='catalogcampaign',
            name='end_datetime',
            field=models.DateTimeField(blank=True, help_text='The date and time the campaign ends. This is only applicable if the campaign is marked as active.', null=True, verbose_name='end date and time'),
        ),
        migrations.AlterField(
            model_name='catalogcampaign',
            name='shop',
            field=models.ForeignKey(help_text='The shop where the campaign is active.', on_delete=django.db.models.deletion.CASCADE, to='wshop.Shop', verbose_name='shop'),
        ),
        migrations.AlterField(
            model_name='catalogcampaign',
            name='start_datetime',
            field=models.DateTimeField(blank=True, help_text='The date and time the campaign starts. This is only applicable if the campaign is marked as active.', null=True, verbose_name='start date and time'),
        ),
        migrations.AlterField(
            model_name='catalogcampaigntranslation',
            name='public_name',
            field=models.CharField(blank=True, help_text='The campaign name to show in the store front.', max_length=120),
        ),
        migrations.AlterField(
            model_name='categoryproductsbasketcondition',
            name='categories',
            field=models.ManyToManyField(related_name='_categoryproductsbasketcondition_categories_+', to='wshop.Category', verbose_name='categories'),
        ),
        migrations.AlterField(
            model_name='categoryproductsbasketcondition',
            name='excluded_categories',
            field=models.ManyToManyField(blank=True, help_text="If the customer has even a single product in the basket from these categories this rule won't match thus the campaign cannot be applied to the basket.", related_name='_categoryproductsbasketcondition_excluded_categories_+', to='wshop.Category', verbose_name='excluded categories'),
        ),
    ]