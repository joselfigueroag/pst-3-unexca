# Generated by Django 4.2.3 on 2024-04-21 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_country_is_deleted_municipality_is_deleted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='municipality',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='parish',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='state',
            name='is_deleted',
        ),
    ]
