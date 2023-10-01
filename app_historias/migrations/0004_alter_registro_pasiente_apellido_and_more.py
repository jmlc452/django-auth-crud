# Generated by Django 4.2.4 on 2023-08-31 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_historias', '0003_alter_registro_pasiente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro_pasiente',
            name='apellido',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registro_pasiente',
            name='direccion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registro_pasiente',
            name='edad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registro_pasiente',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='registro_pasiente',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registro_pasiente',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='registro_pasiente',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registro_pasiente',
            name='peso',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registro_pasiente',
            name='referido',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registro_pasiente',
            name='talla',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
