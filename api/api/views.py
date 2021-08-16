from django.http import JsonResponse, HttpResponse

from api.models import RequisitionCredit
from api.errors_validation import check_errors
from api.thread import ThreadGetValidation

import json, uuid, logging

# Get an instance of a logger
logger = logging.getLogger('django')

def sendRequestCredit(request):
    """View de solicitação de pedido de crédito"""

    if request.method == 'POST':
        logger.info('Requisicao de solicitacao de credito recebida')
        try: 
            jsonRequest = json.loads(request.body.decode('utf-8')) #Pega os dados do corpo da requisição
            logger.info('Dados no corpo da requisicao: '+ str(jsonRequest))
        except: 

            logger.error('Erro ao carregar os dados da requisicao')
            return JsonResponse({"Errors": 'Erro ao enviar sua solicitação'},status=415)

        errors = check_errors(jsonRequest) #Executa a função de checkar erros e retorna uma lista contendo esses erros

        if errors:
            logger.error('Erro na verificacao dos dados')
            return JsonResponse({"Errors": errors}, status=422)

        try: 
            #Se não há erros é feito, é feito um tratamento de exceção dos processos a a seguir
            ticket_id = uuid.uuid4() #Gera um id unico para o ticket
            logger.info('ticket gerado: '+ str(ticket_id))

            logger.warning('Iniciando validacao assincrona')
            ThreadGetValidation(request, jsonRequest, ticket_id,).start() #Executa uma thread assincrona para fazer a validação dos dados sem precisar esperar pela thread principal terminar
            
            logger.info('Inserindo o registro no banco de dados')
            data = RequisitionCredit.objects.create(ticket_id=ticket_id, **jsonRequest)  #insere no banco de dados, os dados da requisição

            logger.info('Insersao realizado com sucesso')
            return JsonResponse({'ticket': ticket_id}, status=201) # Retorna o id do ticket

        except:
            #Se aconteceu algum problema, comportamento inesperado durante o try. É disparado o except, e retornado uma mensagem que não foi possivel processar a solicitação
            logger.critical('Erro interno do sistema')
            return JsonResponse({'Error': 'Erro ao processar sua solicitação'},status=500)


def queryRequestCredit(request, ticket_id):
    """View de consulta do pedido de crédito"""
    if request.method == 'GET':
        logger.info('Requisicao de consultar status recebida')
        logger.info('Ticket recebido: ' + ticket_id)
        status_credit = RequisitionCredit.objects.filter(ticket_id=ticket_id).values_list('status', flat=True).first()

        if not status_credit:
            logger.error('O Ticket informado não existe')
            return JsonResponse({'Error': 'O Ticket informado não existe'},status=404)
        
        logger.info('Status da consulta ao banco: ' + str(status_credit))
        return JsonResponse({'Status': status_credit}, status=202)
    
            

