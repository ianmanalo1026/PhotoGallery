# Generated by Django 3.1.1 on 2020-12-04 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_auto_20201204_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergallery',
            name='photo',
            field=models.ImageField(upload_to='images'),
        ),
    ]
