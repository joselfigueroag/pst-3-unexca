# Generated by Django 4.2.3 on 2023-11-06 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_data', '0011_sectiongradeshift'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='group',
            field=models.CharField(max_length=2, unique=True, verbose_name='grupo'),
        ),
    ]