# Generated by Django 3.1.7 on 2021-03-29 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0003_auto_20210329_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.FloatField()),
                ('stock', models.IntegerField()),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='personas.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('montoTotal', models.FloatField()),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='personas.cliente')),
                ('peluquero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='personas.peluquero')),
            ],
        ),
        migrations.CreateModel(
            name='VentaDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precioUnit', models.FloatField()),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.articulo')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.venta')),
            ],
        ),
    ]
