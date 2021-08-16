from datetime import datetime

list_of_errors = []

def verify_cpf(data):
    
    cpf = data['cpf']

    if len(cpf) != 11 or not cpf:
        list_of_errors.append('CPF inválido')

def verify_name(data):
    name = data['name']

    if not name:
        list_of_errors.append('Nome não pode ser em branco')

def verify_birth_date(data):
    birth_date = data['birth_date']

    # if len(birth_date) != 10 or not birth_date:
    #     list_of_errors.append('Data de nascimento inválida')

    try:
        bool(datetime.strptime(birth_date, '%Y-%m-%d'))
    except ValueError:
        list_of_errors.append('Data de nascimento inválida')


    
    
def verify_value_credit(data):
    value_credit = data['value_credit']

    value_credit = value_credit.replace('.','',1)

    if not value_credit.isdigit():
        list_of_errors.append('Valor do crédito está inválido')


def clear_list_of_errors():
    global list_of_errors
    list_of_errors = []


def check_errors(data):

    clear_list_of_errors()

    verify_name(data)
    verify_cpf(data)
    verify_birth_date(data)
    verify_value_credit(data)

    return list_of_errors
       


