# Generated by Django 4.2.3 on 2024-04-21 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0013_country_deleted_at_country_restored_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shift',
            name='restored_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]