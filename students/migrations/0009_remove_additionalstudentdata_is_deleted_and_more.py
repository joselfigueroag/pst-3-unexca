# Generated by Django 4.2.3 on 2024-04-21 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_additionalstudentdata_is_deleted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additionalstudentdata',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='representative',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_deleted',
        ),
    ]
