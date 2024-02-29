# Generated by Django 4.2.3 on 2024-02-29 04:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0006_make_view_student_detail"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentDetail",
            fields=[
                (
                    "student_id",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="estudiante"
                    ),
                ),
                (
                    "sp_nombre",
                    models.CharField(max_length=50, verbose_name="sp_nombre"),
                ),
                (
                    "ss_nombre",
                    models.CharField(max_length=50, verbose_name="ss_nombre"),
                ),
                (
                    "sp_apellido",
                    models.CharField(max_length=50, verbose_name="sp_apellido"),
                ),
                (
                    "ss_apellido",
                    models.CharField(max_length=50, verbose_name="sp_apellido"),
                ),
                ("s_cedula", models.CharField(max_length=50, verbose_name="s_cedula")),
                ("genero", models.CharField(max_length=20, verbose_name="genero")),
                ("peso", models.CharField(max_length=10, verbose_name="peso")),
                ("talla", models.CharField(max_length=10, verbose_name="talla")),
                ("tlf_stu", models.CharField(max_length=50, verbose_name="tlf_stu")),
                (
                    "rp_nombre",
                    models.CharField(max_length=50, verbose_name="rp_nombre"),
                ),
                (
                    "rs_nombre",
                    models.CharField(max_length=50, verbose_name="rs_nombre"),
                ),
                (
                    "rp_apellido",
                    models.CharField(max_length=50, verbose_name="rp_apellido"),
                ),
                (
                    "rs_apellido",
                    models.CharField(max_length=50, verbose_name="rs_apellido"),
                ),
                ("r_cedula", models.CharField(max_length=50, verbose_name="r_cedula")),
                ("tlf_rep", models.CharField(max_length=50, verbose_name="tlf_rep")),
                ("r_correo", models.CharField(max_length=50, verbose_name="correo")),
                (
                    "periodo_id",
                    models.CharField(max_length=50, verbose_name="periodo_id"),
                ),
                ("periodo", models.CharField(max_length=50, verbose_name="periodo")),
                ("ano", models.CharField(max_length=50, verbose_name="ano")),
                ("seccion", models.CharField(max_length=50, verbose_name="seccion")),
            ],
            options={
                "db_table": "student_detail_all",
                "managed": False,
            },
        ),
    ]