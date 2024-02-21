# Generated by Django 4.2.3 on 2023-11-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_data', '0014_alter_teacher_identity_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('period', models.CharField(max_length=9, unique=True, verbose_name='periodo')),
            ],
            options={
                'verbose_name': 'periodo academico',
                'verbose_name_plural': 'periodos academicos',
            },
        ),
        migrations.DeleteModel(
            name='SectionGradeShift',
        ),
    ]