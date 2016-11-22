# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_test', '0002_auto_20161122_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='typeId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web_test.UserType'),
            preserve_default=False,
        ),
    ]
