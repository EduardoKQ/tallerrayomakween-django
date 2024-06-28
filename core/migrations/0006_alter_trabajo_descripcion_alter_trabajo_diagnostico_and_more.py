# Generated by Django 5.0.6 on 2024-06-28 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_trabajo_foto_principal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajo',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='diagnostico',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='revision',
            field=models.CharField(choices=[('Por revisar', 'Por revisar'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado'), ('Inactivo', 'Inactivo')], max_length=100),
        ),
    ]
