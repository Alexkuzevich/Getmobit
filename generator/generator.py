from faker import Faker
from data.data import User

faker_en = Faker('En')


def generated_user():
    return User(
        name=faker_en.name(),
        email=faker_en.email(),
        password=faker_en.password(),
        birthday=faker_en.random_int(min=10012001, max=10012009, step=1),
        gender="Мужской",
        startday=faker_en.random_int(min=10012001, max=10012009, step=1),
        hobby=faker_en.text(),
        name1=faker_en.first_name(),
        surname1=faker_en.last_name(),
        father1=faker_en.first_name(),
        cat=faker_en.text(max_nb_chars=5),
        dog=faker_en.text(max_nb_chars=5),
        parrot=faker_en.text(max_nb_chars=5),
        cavy=faker_en.text(max_nb_chars=5),
        hamster=faker_en.text(max_nb_chars=5),
        squirrel=faker_en.text(max_nb_chars=5),
        phone=faker_en.phone_number(),
        address=faker_en.text(max_nb_chars=5),
        inn=faker_en.random_int(min=100, max=100000, step=5),

    )
