# Generated by Django 4.2.3 on 2024-02-21 02:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("academic_data", "0024_alter_qualification_note"),
    ]

    operations = [
        migrations.AddField(
            model_name="grade",
            name="subjects",
            field=models.ManyToManyField(
                to="academic_data.subject", verbose_name="materias"
            ),
        ),
    ]
