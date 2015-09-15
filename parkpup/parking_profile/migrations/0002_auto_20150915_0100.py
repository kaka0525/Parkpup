# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
