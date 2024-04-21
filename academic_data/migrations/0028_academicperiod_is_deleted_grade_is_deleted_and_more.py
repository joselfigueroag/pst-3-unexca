# Generated by Django 4.2.3 on 2024-04-21 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_data', '0027_allnotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicperiod',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='grade',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='qualification',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='section',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subject',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tuition',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
