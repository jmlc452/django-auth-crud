# Generated by Django 4.2.4 on 2023-08-31 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_historias', '0006_alter_registro_pasiente_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro_historia',
            name='creacion',
            field=models.DateField(auto_now_add=True),
        ),
    ]
