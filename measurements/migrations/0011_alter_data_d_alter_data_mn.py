# Generated by Django 4.1.4 on 2023-09-27 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0010_data_d_data_mn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='d',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='mn',
            field=models.CharField(max_length=100, null=True),
        ),
    ]