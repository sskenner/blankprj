# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-09 01:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurant_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurant',
            new_name='RestaurantLocation',
        ),
    ]
