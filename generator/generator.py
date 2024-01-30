from faker import Faker
from data.data import User

faker_en = Faker('En')


def generated_user():
    return User(
        name=faker_en.name(),
        email=faker_en.email(),
        password=faker_en.password(),

    )