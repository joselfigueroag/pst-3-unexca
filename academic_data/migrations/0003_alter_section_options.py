# Generated by Django 4.2.3 on 2023-10-28 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic_data', '0002_grade_section'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': 'seccion', 'verbose_name_plural': 'secciones'},
        ),
    ]
