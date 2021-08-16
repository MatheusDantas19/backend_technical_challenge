from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse

import json

client = Client()

class TestAPI(TestCase):        

    def test_post_request_credit(self):

        self.valid_payload = {
            'name': 'Matheus',
            'cpf': '01234567891',
            'birth_date': '1999-05-31',
            'value_credit': '5000',
        }

        response = client.post(
            reverse('post_credit'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)

    def test_payload_nome_is_empty(self):
        self.valid_payload = {
            'name': '',
            'cpf': '01234567891',
            'birth_date': '1999-05-31',
            'value_credit': '100001',
        }

        response_post = client.post(
            reverse('post_credit'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )

        errors = response_post.json()['Errors']

        self.assertEqual(response_post.status_code, 422)
        self.assertIn('Nome não pode ser em branco', errors)

    def test_payload_cpf_is_empty(self):
        self.valid_payload = {
            'name': 'Teteu',
            'cpf': '',
            'birth_date': '1999-05-31',
            'value_credit': '100001',
        }

        response_post = client.post(
            reverse('post_credit'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )

        errors = response_post.json()['Errors']

        self.assertEqual(response_post.status_code, 422)
        self.assertIn('CPF inválido', errors)

    def test_payload_birth_date_is_invalid(self):
        self.valid_payload = {
            'name': 'Matheus',
            'cpf': '01234567891',
            'birth_date': '1999-05-36',
            'value_credit': '100001',
        }
        
        response_post = client.post(
            reverse('post_credit'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )

        errors = response_post.json()['Errors']

        self.assertEqual(response_post.status_code, 422)
        self.assertIn('Data de nascimento inválida', errors)
    
    def test_payload_value_credit_is_negative(self):
        self.valid_payload = {
            'name': 'matheus',
            'cpf': '01234567891',
            'birth_date': '1999-05-31',
            'value_credit': '-123',
        }

        response_post = client.post(
            reverse('post_credit'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )

        errors = response_post.json()['Errors']

        self.assertEqual(response_post.status_code, 422)
        self.assertIn('Valor do crédito está inválido', errors)

    def test_payload_all_empty(self):
        self.valid_payload = {
            'name': '',
            'cpf': '',
            'birth_date': '',
            'value_credit': '',
        }

        response_post = client.post(
            reverse('post_credit'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        errors = response_post.json()['Errors']

        list_of_errors = ['Nome não pode ser em branco', 'CPF inválido','Data de nascimento inválida','Valor do crédito está inválido']

        self.assertEqual(response_post.status_code, 422)
        self.assertEqual(list_of_errors, errors)


