# Generated by Django 4.2.3 on 2024-02-28 14:06

from django.db import migrations

CREATE_SQL = """
    -- View: public.student_detail_all

    -- DROP VIEW public.student_detail_all;

    CREATE OR REPLACE VIEW public.student_detail_all
     AS
        SELECT stu.id AS student_id,
            stu.first_name AS sp_nombre,
            stu.second_name AS ss_nombre,
            stu.first_surname AS sp_apellido,
            stu.second_surname AS ss_apellido,
            stu.identity_card AS s_cedula,
            gen.name AS genero,
            dat.weight AS peso,
            dat.size AS talla,
            dat.phone_number AS tlf_stu,
            rep.first_name AS rp_nombre,
            rep.second_name AS rs_nombre,
            rep.first_surname AS rp_apellido,
            rep.second_surname AS rs_apellido,
            rep.identity_card AS r_cedula,
            rep.phone_number AS tlf_rep,
            rep.email AS r_correo,
            per.id AS periodo_id,
            per.period AS periodo,
            gra.year AS ano,
            sec."group" AS seccion
        FROM students_student stu
            LEFT JOIN common_gender gen ON stu.gender_id = gen.id
            LEFT JOIN students_additionalstudentdata dat ON stu.id = dat.student_id
            LEFT JOIN students_representative rep ON stu.representative_id = rep.id
            LEFT JOIN academic_data_tuition_students adt ON stu.id = adt.student_id
            LEFT JOIN academic_data_tuition tui ON adt.tuition_id = tui.id
            LEFT JOIN academic_data_academicperiod per ON tui.academic_period_id = per.id
            LEFT JOIN academic_data_grade gra ON tui.grade_id = gra.id
            LEFT JOIN academic_data_section sec ON tui.section_id = sec.id;

    ALTER TABLE public.student_detail_all
        OWNER TO postgres;
    COMMENT ON VIEW public.student_detail_all
        IS 'Vista para extraer la infromacion detallada del estudiante';
"""

DROP_SQL = "drop view if exists public.student_detail_all"

class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_additionalstudentdata_options_and_more'),
    ]

    operations = [
        migrations.RunSQL(
            sql=CREATE_SQL,
            reverse_sql=DROP_SQL,
        ),
    ]