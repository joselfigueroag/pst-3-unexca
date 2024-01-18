# Generated by Django 4.2.3 on 2024-01-17 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_moment'),
        ('academic_data', '0020_qualification'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualification',
            name='moment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='common.moment', verbose_name='momento'),
        ),
    ]
