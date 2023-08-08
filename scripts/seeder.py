from django.contrib.auth.models import Group
from common.models import Country, State, Parish, Municipality
import json
import os

json_file=os.path.join(os.path.dirname(__file__),"venezuela.json")
country_name='Venezuela'

def run():
    if not Group.objects.all():
        groups = ["admin", "control_estudio", "evaluacion", "coordinacion", "docente"]

        bulk_list_groups = []
        for group in groups:
            bulk_list_groups.append(Group(name=group))

        Group.objects.bulk_create(bulk_list_groups)

    if not Country.objects.all():
            print('seed directions for',country_name,' to data base')
            new_country = Country.objects.create(name=country_name)
            with open(json_file, 'r') as output:
                data = json.load(output)
                for state in data:
                    new_state = State.objects.create(name=state['estado'],capital=state['capital'],country=new_country)
                    for municipio in state['municipios']:
                        new_municipality = Municipality.objects.create(name=municipio['municipio'],state=new_state)
                        for parroquias in municipio['parroquias']:
                            new_parish = Parish.objects.create(name=parroquias,municipality=new_municipality)
            print('end')
    else:
        print('ya existe el registro')