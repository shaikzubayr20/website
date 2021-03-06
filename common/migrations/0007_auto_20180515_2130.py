# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-15 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20170418_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content_markup_type',
            field=models.CharField(choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain'), ('restructuredtext', 'Restructured Text')], default='restructuredtext', editable=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='uploaded_file',
            field=models.FileField(upload_to='uploads'),
        ),
    ]
