# Generated by Django 4.1.2 on 2022-12-08 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0006_user_tanggal_lahir'),
    ]

    operations = [
        migrations.AddField(
            model_name='postingan',
            name='destinasi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tours.destinasi'),
        ),
    ]
