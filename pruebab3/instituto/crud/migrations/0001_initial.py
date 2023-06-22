# Generated by Django 4.2.2 on 2023-06-22 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('idMarca', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, null=True, unique=True)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipoproducto',
            fields=[
                ('idtTipoproducto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, null=True, unique=True)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False)),
                ('nombreProducto', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.CharField(max_length=50, unique=True)),
                ('marcaProducto', models.CharField(max_length=50, unique=True)),
                ('precio', models.CharField(default='', max_length=999999)),
                ('stock', models.CharField(default='', max_length=1000)),
                ('activo', models.BooleanField()),
                ('Marca', models.ForeignKey(blank=True, db_column='idMarca', null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.marca')),
                ('Tipoproducto', models.ForeignKey(blank=True, db_column='idtTipoproducto', null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.tipoproducto')),
            ],
        ),
    ]
