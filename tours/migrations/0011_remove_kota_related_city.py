# Generated by Django 4.1.2 on 2022-12-08 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0010_remove_destinasi_album_delete_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kota',
            name='related_city',
        ),
    ]