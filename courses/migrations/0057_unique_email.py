# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-25 17:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0056_remove_userena'),
    ]

    operations = [
        migrations.RunSQL(
            "create unique index auth_user_email_uindex on auth_user (email);"
        )
    ]