# Generated by Django 4.0.6 on 2022-07-28 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appventas', '0002_alter_bicicletas_rodado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bicicletas',
            name='fecha_fabricacion',
        ),
        migrations.RemoveField(
            model_name='repuestos',
            name='fecha_fabricacion',
        ),
    ]
