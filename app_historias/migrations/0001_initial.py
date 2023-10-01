# Generated by Django 4.2.4 on 2023-08-30 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_Pasiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_nacimiento', models.DateField()),
                ('edad', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('direccion', models.CharField(max_length=100)),
                ('referido', models.CharField(max_length=50)),
                ('peso', models.FloatField()),
                ('talla', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'registro_pasiente',
                'verbose_name_plural': 'registro_pasientes',
            },
        ),
        migrations.CreateModel(
            name='Registro_Historia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('historia', models.TextField()),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('pasiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_historias.registro_pasiente')),
            ],
            options={
                'verbose_name': 'Registro_Historia',
                'verbose_name_plural': 'Registro_Historias',
            },
        ),
    ]
