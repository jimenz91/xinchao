# Generated by Django 3.2.3 on 2021-05-23 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_remove_table_orders_placed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='dish',
            name='weight',
            field=models.FloatField(),
        ),
    ]
