# Generated by Django 5.0.1 on 2024-01-23 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_diary_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='created',
            field=models.CharField(default=datetime.datetime.utcnow, max_length=128),
        ),
    ]
