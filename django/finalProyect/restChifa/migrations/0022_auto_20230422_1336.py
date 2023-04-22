# Generated by Django 3.2.18 on 2023-04-22 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restChifa', '0021_alter_reserve_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='number_people',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='other',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
