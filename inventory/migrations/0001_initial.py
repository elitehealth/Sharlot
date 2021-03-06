# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('note1', models.CharField(blank=True, max_length=100)),
                ('note2', models.CharField(blank=True, max_length=100)),
                ('note3', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_type', models.CharField(max_length=75)),
                ('measure', models.CharField(blank=True, max_length=100)),
                ('note1', models.CharField(blank=True, max_length=100)),
                ('note2', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('contact_name', models.CharField(max_length=75)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('bank_account', models.CharField(blank=True, max_length=100)),
                ('note1', models.CharField(blank=True, max_length=100)),
                ('note2', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='add_inventory',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory'),
        ),
        migrations.AddField(
            model_name='add_inventory',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier'),
        ),
    ]
