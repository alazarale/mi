# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('photo', models.ImageField(upload_to='product/image/')),
                ('description', models.TextField(max_length='1000')),
                ('price', models.FloatField()),
                ('quantity', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('publish', 'Publish'), ('cancel', 'Cancel')], max_length=7)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
