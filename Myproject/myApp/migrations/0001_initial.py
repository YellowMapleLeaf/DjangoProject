# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-13 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=20)),
                ('fSex', models.BooleanField(default=True)),
                ('fAge', models.IntegerField()),
                ('fSingle', models.BooleanField(default=True)),
            ],
        ),
    ]