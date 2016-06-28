# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_postmodel_upload'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'ordering': ['-timestamp', '-updated']},
        ),
        migrations.AddField(
            model_name='postmodel',
            name='image',
            field=models.FileField(null=True, blank=True, upload_to=''),
        ),
    ]
