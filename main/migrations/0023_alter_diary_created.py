# Generated by Django 5.0.1 on 2024-01-23 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_remove_diary_color_alter_diary_created_delete_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='created',
            field=models.CharField(default='capy', max_length=128),
        ),
    ]
