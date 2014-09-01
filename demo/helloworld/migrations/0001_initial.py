# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewflow', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelloWorldProcess',
            fields=[
                ('process_ptr', models.OneToOneField(primary_key=True, to='viewflow.Process', auto_created=True, serialize=False)),
                ('text', models.CharField(max_length=250)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=('viewflow.process',),
        ),
    ]
