# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Record',
                'verbose_name_plural': 'Records',
            },
        ),
        migrations.CreateModel(
            name='RecordProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('property', models.ForeignKey(to='repositories.Property')),
                ('record', models.ForeignKey(to='repositories.Record')),
            ],
            options={
                'verbose_name': 'RecordProperty',
                'verbose_name_plural': 'RecordProperties',
            },
        ),
        migrations.CreateModel(
            name='RecordSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('record', models.ForeignKey(to='repositories.Record')),
            ],
            options={
                'verbose_name': 'RecordSet',
                'verbose_name_plural': 'RecordSets',
            },
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Repository',
                'verbose_name_plural': 'Repositories',
            },
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('repository', models.ForeignKey(to='repositories.Repository')),
            ],
            options={
                'verbose_name': 'Set',
                'verbose_name_plural': 'Sets',
            },
        ),
        migrations.AddField(
            model_name='recordset',
            name='set',
            field=models.ForeignKey(to='repositories.Set'),
        ),
        migrations.AddField(
            model_name='record',
            name='repository',
            field=models.ForeignKey(to='repositories.Repository'),
        ),
    ]
