from datetime import datetime, date
list_of_errors = []

def clean_list_of_errors():
    global list_of_errors
    list_of_errors = []


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def verify_birth_day(data):
    birth_day = data['birth_date']
    birth_day = datetime.strptime(birth_day, "%Y-%m-%d")

    age = calculate_age(birth_day)

    if age < 18:
        list_of_errors.append('Idade incompatível')
 

def verify_value_credit(data):
    value_credit = float(data['value_credit'])

    if value_credit < 1 or value_credit > 100000:
        list_of_errors.append('Valor incompatível')


def main(data):
    clean_list_of_errors()

    verify_birth_day(data)
    verify_value_credit(data)

    return list_of_errors