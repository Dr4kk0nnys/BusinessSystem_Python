def get_client_info():

    name = input('Name: ')
    cpf = input('CPF: ')
    phone_number = input('Phone number: ')
    adress = input('Adress: ')

    return {
        'name': name,
        'cpf': cpf,
        'phone_number': phone_number,
        'adress': adress
    }
