# Generated by Django 5.0.1 on 2024-01-22 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_diary_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='name',
            field=models.CharField(default='color', max_length=128),
        ),
    ]
