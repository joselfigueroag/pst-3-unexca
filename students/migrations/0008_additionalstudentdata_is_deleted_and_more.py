# Generated by Django 4.2.3 on 2024-04-21 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_studentdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionalstudentdata',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='representative',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
