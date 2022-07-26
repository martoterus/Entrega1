# Generated by Django 4.0.6 on 2022-07-25 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bicicletas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('rodado', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('fecha_fabricacion', models.DateField()),
                ('precio', models.IntegerField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='indumentaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('talle', models.CharField(max_length=30)),
                ('precio', models.IntegerField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='repuestos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('fabricante', models.CharField(max_length=30)),
                ('fecha_fabricacion', models.DateField()),
                ('precio', models.IntegerField(max_length=30)),
            ],
        ),
    ]
