# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('tag1', models.CharField(max_length=250)),
                ('tag2', models.CharField(max_length=250)),
                ('num_typo1', models.IntegerField(default=0)),
                ('num_typo2', models.IntegerField(default=0)),
                ('avg_length1', models.IntegerField(default=0)),
                ('avg_length2', models.IntegerField(default=0)),
                ('frequency1', models.IntegerField(default=0)),
                ('frequency2', models.IntegerField(default=0)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('Initiated', 'Initiated'), ('Started', 'Started'), ('Finished', 'Finished')], default='Initiated', max_length=20)),
                ('compare', models.CharField(choices=[('Number of typos', 'Number of typos'), ('Length of tweets', 'Length of tweets'), ('Frequency of tweets', 'Frequency of tweets')], default='Number of typos', max_length=50)),
            ],
        ),
    ]
