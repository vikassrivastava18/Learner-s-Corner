# Generated by Django 2.0.3 on 2018-12-06 15:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(help_text='ask aquestion', max_length=200)),
                ('date', models.DateField(blank=True, default=datetime.date(2018, 12, 6), null=True)),
                ('status', models.CharField(choices=[('p', 'Pending'), ('r', 'Resolved')], help_text='Status of Question Asked', max_length=1)),
                ('asked_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
