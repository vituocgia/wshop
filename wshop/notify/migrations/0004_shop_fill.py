# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def fill_shop_scripts(apps, schema_editor):
    Script = apps.get_model("wshop_notify", "Script")
    Notification = apps.get_model("wshop_notify", "Notification")
    Shop = apps.get_model("wshop", "Shop")

    main_shop = Shop.objects.first()
    Script.objects.update(shop=main_shop)
    Notification.objects.update(shop=main_shop)


class Migration(migrations.Migration):

    dependencies = [
        ('wshop_notify', '0002_shop_scripts')
    ]

    operations = [
        migrations.RunPython(fill_shop_scripts, migrations.RunPython.noop)
    ]
