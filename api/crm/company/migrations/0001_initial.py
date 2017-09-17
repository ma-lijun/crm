# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 03:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('uid', models.CharField(db_index=True, max_length=4, primary_key=True, serialize=False, unique=True)),
                ('seq', models.IntegerField(unique=True)),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('description', markdownx.models.MarkdownxField(blank=True, db_index=True, max_length=10000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('isuser', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies_owned_by', to='contact.Contact', verbose_name='owner')),
                ('owner_backup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companies_backedup_by', to='contact.Contact', verbose_name='owner_backup')),
                ('users', models.ManyToManyField(related_name='companies', to='contact.Contact')),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='CompanyEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(db_index=True, max_length=40)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='company.Company', verbose_name='company')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(db_index=True, max_length=15)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_numbers', to='company.Company', verbose_name='company')),
            ],
        ),
    ]