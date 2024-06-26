# Generated by Django 4.2.3 on 2024-04-21 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0013_country_deleted_at_country_restored_at_and_more'),
        ('academic_data', '0030_academicperiod_deleted_at_academicperiod_restored_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuition',
            name='shift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.shift', verbose_name='turno'),
        ),
    ]
