# Generated by Django 2.2.10 on 2020-06-11 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200610_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plusphoto',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
