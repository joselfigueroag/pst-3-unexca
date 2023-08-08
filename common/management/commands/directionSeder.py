from django.core.management.base import BaseCommand
from common.models import Country, State, Parish, Municipality
import json
import os

json_file=os.path.join(os.path.dirname(__file__),"venezuela.json")
country_name='Venezuela'

class Command(BaseCommand):
    help = 'Seed for directions of Venezuela to data base'
    
    def handle(self, *args, **options):
        if not Country.objects.all():
            new_country = Country.objects.create(name=country_name)
            print(new_country)
        """with open(json_file, 'r') as output:
            data = json.load(output)
            for item in data:
                print(item['estado'])"""
        self.stdout.write(self.style.SUCCESS('Comando ejecutado exitosamente'))

