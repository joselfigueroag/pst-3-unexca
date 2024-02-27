# Generated by Django 4.2.3 on 2024-02-23 03:01

from django.db import migrations

CREATE_SQL = """ 
    CREATE OR REPLACE VIEW public.academic_notes_all
    AS
      SELECT DISTINCT 
        stu.id AS student_id,
        aca.id AS matricula,
        stu.first_name AS p_nombre,
        stu.second_name AS s_nombre,
        stu.first_surname AS p_apellido,
        stu.second_surname AS s_apellido,
        stu.identity_card AS cedula,
        gra.year AS grado,
        sec."group" AS seccion,
        tur.turn AS turno,
        per.period AS periodo,
        sub.id AS id_asignacion,
        sub.name AS asignacion,
        CASE
            WHEN qua1.note IS NOT NULL AND qua1.student_id = stu.id THEN qua1.note
            ELSE NULL::numeric
        END AS momento1,
        CASE
            WHEN qua2.note IS NOT NULL AND qua2.student_id = stu.id THEN qua2.note
            ELSE NULL::numeric
        END AS momento2,
        CASE
            WHEN qua3.note IS NOT NULL AND qua3.student_id = stu.id THEN qua3.note
            ELSE NULL::numeric
        END AS momento3,
        round((COALESCE(qua1.note, 0::numeric) + COALESCE(qua2.note, 0::numeric) + COALESCE(qua3.note, 0::numeric)) / 3.0, 1) AS definitiva
    FROM students_student stu
        INNER JOIN academic_data_tuition_students ate ON ate.student_id = stu.id
        INNER JOIN academic_data_tuition aca ON ate.tuition_id = aca.id
        INNER JOIN academic_data_grade gra ON aca.grade_id = gra.id
        INNER JOIN academic_data_section sec ON sec.id = aca.section_id
        INNER JOIN academic_data_academicperiod per ON per.id = aca.academic_period_id
        INNER JOIN common_shift tur ON tur.id = aca.shift_id
        LEFT JOIN academic_data_subject sub ON 1 = 1
        LEFT JOIN academic_data_qualification qua1 ON qua1.subject_id = sub.id AND qua1.student_id = stu.id AND qua1.moment_id = 1
        LEFT JOIN academic_data_qualification qua2 ON qua2.subject_id = sub.id AND qua2.student_id = stu.id AND qua2.moment_id = 2
        LEFT JOIN academic_data_qualification qua3 ON qua3.subject_id = sub.id AND qua3.student_id = stu.id AND qua3.moment_id = 3;

    ALTER TABLE public.academic_notes_all
    OWNER TO postgres;
"""

DROP_SQL = "drop view if exists public.academic_notes_all"

class Migration(migrations.Migration):
    dependencies = [
        ("academic_data", "0025_grade_subjects"),
    ]

    operations = [
        migrations.RunSQL(
            sql=CREATE_SQL,
            reverse_sql=DROP_SQL,
        ),
    ]
