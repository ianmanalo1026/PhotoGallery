# Generated by Django 3.1.1 on 2020-12-04 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20201204_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='introduction',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]