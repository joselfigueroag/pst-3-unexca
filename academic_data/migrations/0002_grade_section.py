# Generated by Django 4.2.3 on 2023-10-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('year', models.CharField(max_length=3, verbose_name='año')),
            ],
            options={
                'verbose_name': 'grado',
                'verbose_name_plural': 'grados',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group', models.CharField(max_length=2, verbose_name='grupo')),
            ],
            options={
                'verbose_name': 'grupo',
                'verbose_name_plural': 'grupos',
            },
        ),
    ]
