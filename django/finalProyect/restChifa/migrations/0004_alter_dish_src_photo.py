# Generated by Django 3.2.18 on 2023-04-07 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restChifa', '0003_alter_dish_src_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='src_photo',
            field=models.ImageField(default='no_image.jpg', upload_to=''),
        ),
    ]
