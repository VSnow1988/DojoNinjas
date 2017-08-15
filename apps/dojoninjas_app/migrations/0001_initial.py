# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 01:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dojo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ninja',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('dojo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dojoninjas_app.Dojo')),
            ],
        ),
    ]