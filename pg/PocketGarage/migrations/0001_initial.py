# Generated by Django 2.2.8 on 2020-03-23 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CI', models.IntegerField()),
                ('Nombre', models.CharField(max_length=50)),
                ('Telefono', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Modelo', models.CharField(max_length=50)),
                ('Precio', models.CharField(max_length=25)),
                ('Foto', models.ImageField(upload_to='PocketGarage/vehiculos/')),
                ('FichaTecnica', models.CharField(max_length=500)),
                ('Propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PocketGarage.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=200)),
                ('Foto', models.ImageField(upload_to='PocketGarage/repuestos/')),
                ('Precio', models.CharField(max_length=25)),
                ('Vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PocketGarage.Usuario')),
            ],
        ),
    ]