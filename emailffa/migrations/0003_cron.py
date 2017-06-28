# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 08:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emailffa', '0002_auto_20170421_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cron_text', models.CharField(max_length=200)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emailffa.Job')),
            ],
        ),
    ]