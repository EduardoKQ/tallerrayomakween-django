# Generated by Django 5.0.6 on 2024-06-28 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_trabajo_observaciones_alter_mecanico_especialidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='titulo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
