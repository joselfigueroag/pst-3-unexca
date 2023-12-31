# Generated by Django 4.2.3 on 2023-11-06 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_shift'),
        ('academic_data', '0010_remove_grade_sections'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionGradeShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_data.grade')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_data.section')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.shift')),
            ],
            options={
                'ordering': ['grade', 'section'],
            },
        ),
    ]
