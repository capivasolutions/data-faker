from time import sleep
from faker import Faker
from service import Service


def main():
    faker = Faker()
    service = Service()
    while True:
        transaction = faker.generate_transaction()
        service.send_transaction(transaction)
        sleep(3)


if __name__ == '__main__':
    main()
