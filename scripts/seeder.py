from django.contrib.auth.models import Group
from common.models import Country, State, Parish, Municipality, Gender, Shift, Moment
from academic_data.models import Subject, Grade, Section
from users.models import User
import json
import os

json_file = os.path.join(os.path.dirname(__file__), "venezuela.json")
country_name = "Venezuela"


def run():
    if not Group.objects.all():
        groups = ["admin", "control_estudio", "evaluacion", "coordinacion", "docente", "representante"]

        bulk_list_groups = []
        for group in groups:
            bulk_list_groups.append(Group(name=group))

        Group.objects.bulk_create(bulk_list_groups)
        print("Grupos creados")

    if not Country.objects.all():
        print("seed directions for", country_name, " to data base")
        new_country = Country.objects.create(name=country_name)
        with open(json_file, "r") as output:
            data = json.load(output)
            for state in data:
                new_state = State.objects.create(
                    name=state["estado"], capital=state["capital"], country=new_country
                )
                for municipio in state["municipios"]:
                    new_municipality = Municipality.objects.create(
                        name=municipio["municipio"], state=new_state
                    )
                    for parroquias in municipio["parroquias"]:
                        new_parish = Parish.objects.create(
                            name=parroquias, municipality=new_municipality
                        )
        print("Informacion de direccion creada")

    if not Gender.objects.all():
        genders = ["femenino", "masculino"]

        for gender in genders:
            Gender.objects.create(name=gender)
        print("Generos creados")

    if not "admin@admin.com" in User.objects.values_list("email", flat=True):
        group = Group.objects.get(name="admin")
        user = User.objects.create(email="admin@admin.com", group=group)
        user.set_password("12345678.")
        user.save()

    if not Shift.objects.all():
        turns = ["mañana", "tarde"]

        for turn in turns:
            Shift.objects.create(turn=turn)
        print("Turnos creados")

    if not Moment.objects.all():
        moments = ["1er", "2do", "3er"]

        for moment in moments:
            Moment.objects.create(number=moment)
        print("Momentos creados")

    if not Subject.objects.all():
        subjects = [
            "LENGUA Y LITERATURA",
            "IDIOMAS",
            "MATEMATICAS",
            "EDUCACION FISICA",
            "AMBIENTE CIENCIA Y TECNOLOGIA",
            "FISICA",
            "QUIMICA",
            "GEOGRAFIA HISTORIA Y CIUDADANIA",
            "ORIENTACION VOCACIONAL",
            "INNOVACION TECNOLOGICA Y PRODUCTIVA"
        ]
        for subject in subjects:
            Subject.objects.create(name=subject)
        print("Materias Creadas.")

    if not Section.objects.all():
        groups = ["A", "B", "C", "D", "E", "F", "G", "H", "I" ]
        for group in groups:
            Section.objects.create(group=group)
        print('Secciones Creados.') 