# Generated by Django 4.1.2 on 2022-12-08 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_alter_kota_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kota',
            name='description',
        ),
    ]