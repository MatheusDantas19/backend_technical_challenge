from django.shortcuts import render
from django.http import JsonResponse
import json, logging

from validation.check_values import main
# Create your views here.

logger = logging.getLogger('django')

def validation(request):
    if request.method == 'GET':
        logger.info('Requisicao recebida')
        try:
            jsonRequest = json.loads(request.body.decode('utf-8'))
            logger.info('Dados no corpo da requisicao: '+ str(jsonRequest))
        except:
            logger.error('Erro ao ler os dados da requisicao')
            return JsonResponse({"Error":"Não possivel ler os dados da requisição"})

        list_of_errors = main(jsonRequest)

        if not list_of_errors:
            logger.info('Status da avaliação: Aprovado')
            return JsonResponse({'Status':'Aprovado'}, status=201)

        logger.error('Lista de erros: ' + str(list_of_errors))
        logger.warning('Status da avaliação: Reprovado')
        return JsonResponse({'Status':'Rejeitado'}, status=201)
