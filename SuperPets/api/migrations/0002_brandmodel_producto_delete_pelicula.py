# Generated by Django 4.2 on 2023-04-16 16:26

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripción del producto')),
                ('image', models.ImageField(upload_to='products', verbose_name='Imagen')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('amount', models.SmallIntegerField(default=0, verbose_name='Cantidad almacen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.brandmodel', verbose_name='Marca')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['id', 'title'],
            },
        ),
        migrations.DeleteModel(
            name='Pelicula',
        ),
    ]
