import random

from faker import Faker

from students.models import Representative, Student, AdditionalStudentData
from common.models import Gender

fake = Faker(['es_ES'])
genders = Gender.objects.all()
num_digitos = random.choice([7, 8])

def run():
  if not Representative.objects.all():
    bulk_list = []
    for i in range(5):
      gender = random.choice(genders)
      
      if gender.name == "masculino":
        first_name = fake.first_name_male()
        second_name = fake.first_name_male()
        first_surname = fake.last_name_male()
        second_surname = fake.last_name_male()
      else:
        first_name = fake.first_name_female()
        second_name = fake.first_name_female()
        first_surname = fake.last_name_female()
        second_surname = fake.last_name_female()

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
  
  if not Student.objects.all():
    for i in range(5):
      gender = random.choice(genders)
      
      if gender.name == "masculino":
        first_name = fake.first_name_male()
        second_name = fake.first_name_male()
        first_surname = fake.last_name_male()
        second_surname = fake.last_name_male()
      else:
        first_name = fake.first_name_female()
        second_name = fake.first_name_female()
        first_surname = fake.last_name_female()
        second_surname = fake.last_name_female()

      representative = random.choice(Representative.objects.all())

      student = Student.objects.create(
        first_name=first_name,
        second_name=second_name,
        first_surname=first_surname,
        second_surname=second_surname,
        birthday_date=fake.date_of_birth(),
        gender=gender,
        identity_card=fake.random_number(digits=num_digitos),
        representative=representative
      )

      AdditionalStudentData.objects.create(
        student=student,
        email=fake.email(),
        phone_number=fake.phone_number(),
      )
    print("Creados cinco estudiantes de prueba")
