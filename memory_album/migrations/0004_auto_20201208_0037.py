# Generated by Django 3.1.1 on 2020-12-07 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memory_album', '0003_auto_20201208_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergallery',
            name='photographer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]