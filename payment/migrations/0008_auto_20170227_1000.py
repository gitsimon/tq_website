# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_paymentreminder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='state',
            field=models.CharField(choices=[('new', 'new'), ('manual', 'manual'), ('fixed', 'fixed'), ('processed', 'processed')], default='new', max_length=50),
        ),
    ]