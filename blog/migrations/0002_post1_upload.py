# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post1',
            name='upload',
            field=models.ImageField(upload_to='media/', default='media/kitten.jpg'),
        ),
    ]
