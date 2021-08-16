import time, threading, requests
from api.models import RequisitionCredit

import logging

# Get an instance of a logger
logger = logging.getLogger('django')

class ThreadGetValidation (threading.Thread):
    def __init__(self, request, data, ticket_id):
        self.data = data
        self.request = request
        self.ticket_id = ticket_id
        self.url = 'http://validation:3000/validation'

        threading.Thread.__init__(self)

    def run(self):

        validation = self.getValidation(self.data['birth_date'], self.data['value_credit'])

        logger.info('Dados enviados para validacao assincrona:')
        logger.info('Data de aniversario: '+ self.data['birth_date'])
        logger.info('Valor do credito solicitado: '+ self.data['value_credit'])

        status = validation['Status']

        if status == 'Aprovado':
            RequisitionCredit.objects.filter(
                ticket_id=self.ticket_id).update(status='Aprovado')
        else:
            RequisitionCredit.objects.filter(
                ticket_id=self.ticket_id).update(status='Reprovado')

        logger.info('Status da avaliacao: ' + status)
        

    def getValidation(self ,request, birth_date, value_credit):
        time.sleep(10)
       
        res = requests.get(
            self.url, json={'birth_date': birth_date, 'value_credit': value_credit}, verify=False)

        return res.json()
