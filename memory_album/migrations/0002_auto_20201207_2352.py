# Generated by Django 3.1.1 on 2020-12-07 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
        ('memory_album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergallery',
            name='photographer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.profile'),
        ),
    ]
