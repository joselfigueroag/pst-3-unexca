# Generated by Django 4.2.3 on 2023-10-30 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_data', '0003_alter_section_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='sections',
            field=models.ManyToManyField(to='academic_data.section', verbose_name='secciones'),
        ),
    ]