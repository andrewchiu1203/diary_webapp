# Generated by Django 5.0.1 on 2024-01-22 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_diary_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='color',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='main.color'),
        ),
    ]
