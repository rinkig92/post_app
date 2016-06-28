# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20160612_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(upload_to='', height_field='height_field', null=True, blank=True, width_field='width_field'),
        ),
    ]
