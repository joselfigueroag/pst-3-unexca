# Generated by Django 4.2.3 on 2024-01-18 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_moment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name'], 'verbose_name': 'pais', 'verbose_name_plural': 'paises'},
        ),
        migrations.AlterModelOptions(
            name='municipality',
            options={'ordering': ['name'], 'verbose_name': 'municipio', 'verbose_name_plural': 'municipios'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'ordering': ['name'], 'verbose_name': 'estado', 'verbose_name_plural': 'estados'},
        ),
    ]
