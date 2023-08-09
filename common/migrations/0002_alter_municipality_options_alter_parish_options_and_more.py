# Generated by Django 4.2.3 on 2023-08-09 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='municipality',
            options={'verbose_name': 'municipio', 'verbose_name_plural': 'municipios'},
        ),
        migrations.AlterModelOptions(
            name='parish',
            options={'verbose_name': 'parroquia', 'verbose_name_plural': 'parroquias'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name': 'estado', 'verbose_name_plural': 'estados'},
        ),
        migrations.AlterField(
            model_name='municipality',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='municipalities', to='common.state'),
        ),
        migrations.AlterField(
            model_name='parish',
            name='municipality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='parroquia', to='common.municipality'),
        ),
        migrations.AlterField(
            model_name='state',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='states', to='common.country'),
        ),
    ]
