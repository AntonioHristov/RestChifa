# Generated by Django 3.2.18 on 2023-04-07 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restChifa', '0007_auto_20230407_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserve',
            name='date_utc',
        ),
    ]
