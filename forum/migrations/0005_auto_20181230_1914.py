# Generated by Django 2.0.3 on 2018-12-30 13:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20181208_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2018, 12, 30), null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2018, 12, 30), null=True),
        ),
    ]
