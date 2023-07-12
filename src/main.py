from time import sleep
from faker import Faker


def main():
    faker = Faker()
    while True:
        transaction = faker.generate_transaction()
        sleep(3)


if __name__ == '__main__':
    main()
