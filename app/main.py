from faker import Faker

faker = Faker('uk_UA')

def generate_random_contact():
    # Generates and prints a random contact
    full_name = faker.name()
    phone_number = faker.phone_number()
    full_address = faker.address()
    while not phone_number.startswith('+380'):
        phone_number = faker.phone_number()
    print('Information about the person:\n'
          f'Full name: {full_name}\n'
          f'Phone number: {phone_number}\n'
          f'Full address: {full_address}')


def main():
    # The main function of the program
    generate_random_contact()
