import random

from data.data import User
from faker import Faker

faker = Faker()
Faker.seed()

# def generated_user():
#     yield User(
#         full_name= faker.first_name() + " " + faker.last_name(),
#         email= faker.email(),
#         current_address= faker.address(),
#         permanent_address= faker.address(),
#     )

def generated_user():
    while True:  # Loop to make it a true generator for multiple calls
        yield User(
            full_name=faker.first_name() + " " + faker.last_name(),
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            age=random.randint(18, 65),
            salary=random.randint(10000, 100000),
            department=faker.job(),
            email=faker.email(),
            current_address=faker.address().replace('\n', ' '),  # Normalize to single line
            permanent_address=faker.address().replace('\n', ' '),  # Normalize to single line
        )
