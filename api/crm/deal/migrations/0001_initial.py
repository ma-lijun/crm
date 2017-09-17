# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 03:25
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('uid', models.CharField(db_index=True, max_length=4, primary_key=True, serialize=False, unique=True)),
                ('seq', models.IntegerField(unique=True)),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('type', models.CharField(choices=[('hoster', 'hoster'), ('ito', 'ito'), ('pto', 'pto'), ('prepto', 'prepto')], db_index=True, max_length=10)),
                ('state', models.CharField(choices=[('new', 'new'), ('interested', 'interested'), ('confirmed', 'confirmed'), ('waitingclose', 'waitingclose'), ('closed', 'closed')], db_index=True, max_length=20)),
                ('remarks', markdownx.models.MarkdownxField(blank=True, db_index=True, max_length=10000)),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('AED', 'AED'), ('GBP', 'GBP')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('closed_date', models.DateField(blank=True, db_index=True, null=True)),
                ('issuer', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deals', to='company.Company', verbose_name='company')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deals', to='contact.Contact', verbose_name='contact')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deals_owned_by', to='contact.Contact', verbose_name='Owner')),
                ('owner_backup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deals_backedup_by', to='contact.Contact', verbose_name='Backup owner')),
            ],
        ),
    ]