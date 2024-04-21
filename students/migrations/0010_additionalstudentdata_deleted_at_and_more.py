# Generated by Django 4.2.3 on 2024-04-21 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_remove_additionalstudentdata_is_deleted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionalstudentdata',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='additionalstudentdata',
            name='restored_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='representative',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='representative',
            name='restored_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='restored_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]