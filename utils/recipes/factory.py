# from inspect import signature
from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_recipe():
    return {
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=30),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'price_decimal' :  fake.pyfloat(left_digits=3, right_digits=2, min_value=10, max_value=100),
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/book,library' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())