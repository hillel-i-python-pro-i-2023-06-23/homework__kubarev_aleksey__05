from faker import Faker

faker = Faker('uk_UA')

def generate_random_contact():
    # Generates and prints a random contact
    full_name = faker.name()
    phone_number = faker.phone_number()
    while not phone_number.startswith('+380'):
        phone_number = faker.phone_number()
    print(f'ФИО: {full_name}')
    print(f'Номер телефона: {phone_number}')


def main():
    # The main function of the program
    generate_random_contact()
