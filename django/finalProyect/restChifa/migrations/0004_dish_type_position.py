# Generated by Django 3.2.18 on 2023-05-14 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restChifa', '0003_auto_20230513_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish_type',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
