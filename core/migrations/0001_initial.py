# Generated by Django 5.0.6 on 2024-06-27 15:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_especialidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AdministradorTallern',
            fields=[
                ('rut', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mecanico',
            fields=[
                ('rut', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=100)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.especialidad')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_trabajo', models.DateField()),
                ('auto', models.CharField(max_length=100)),
                ('diagnostico', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('revision', models.CharField(choices=[('Por revisar', 'Por revisar'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], max_length=100)),
                ('mecanico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mecanico')),
            ],
        ),
    ]
