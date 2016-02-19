# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('message', models.CharField(max_length=500)),
                ('date', models.DateTimeField()),
                ('url', models.URLField()),
                ('priority', models.IntegerField(default=0)),
                ('read', models.BooleanField(default=False)),
                ('actor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Notification',
            },
        ),
    ]
