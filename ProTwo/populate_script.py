import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()


# Populating DB with content using Faker 

from AppTwo.models import Users_db
from faker import Faker 

fake_gen = Faker()

def populate(N=5):

	for entry in range(N):

		fake_name = fake_gen.name()
		fake_phno = fake_gen.phone_number()
		fake_email = fake_gen.email()

		user_info = Users_db.objects.get_or_create(name=fake_name,phno=fake_phno,email=fake_email)[0]


if __name__ == '__main__':
	print("Please wait till the faker populates the DB")
	populate(10)
	print("Faker populated the DB. You may verify.")
