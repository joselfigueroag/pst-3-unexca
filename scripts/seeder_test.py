import random

from faker import Faker

from students.models import Representative
from common.models import Gender

fake = Faker(['es_ES'])
genders = Gender.objects.values_list("name", flat=True)

def run():
  if not Representative.objects.all():
    bulk_list = []
    for i in range(5):
      gender = random.choice(genders)
      
      if gender == "masculino":
        first_name = fake.first_name_male()
        second_name = fake.first_name_male()
        first_surname = fake.last_name_male()
        second_surname = fake.last_name_male()
      else:
        first_name = fake.first_name_female()
        second_name = fake.first_name_female()
        first_surname = fake.last_name_female()
        second_surname = fake.last_name_female()

      num_digitos = random.choice([7, 8])

      bulk_list.append(Representative(
        first_name=first_name,
        second_name=second_name,
        first_surname=first_surname,
        second_surname=second_surname,
        identity_card=fake.random_number(digits=num_digitos),
        email=fake.email(),
        phone_number=fake.phone_number(),
        address=fake.address(),
      ))

    Representative.objects.bulk_create(bulk_list)
    print("Creados cinco representantes de prueba")
