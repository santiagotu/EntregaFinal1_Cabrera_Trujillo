# Generated by Django 4.1 on 2022-09-10 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Galeria', '0004_remove_avaluador_obra'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaluador',
            name='obra',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Galeria.obra'),
        ),
    ]
