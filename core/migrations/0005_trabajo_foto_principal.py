# Generated by Django 5.0.6 on 2024-06-28 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_trabajo_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='foto_principal',
            field=models.ImageField(null=True, upload_to='fotos/'),
        ),
    ]
