# Generated by Django 4.1.5 on 2023-05-24 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restChifa', '0005_dish_category_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
