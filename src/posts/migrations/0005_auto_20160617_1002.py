# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20160614_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(height_field='height_field', null=True, blank=True, width_field='width_field', upload_to=posts.models.upload_location),
        ),
    ]
