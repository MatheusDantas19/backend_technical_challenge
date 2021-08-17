# Desafio concluído

Esse desafio foi resolvido na linguagem python com o framework Django, que consiste em dois sistemas um é a Api e outro é o Sistema de Validação. <br>

## Rotas da Api
- http://localhost:8000/credit/ -> Rota POST para a solicitação de crédito que são enviado no corpo da requisição.
- http://localhost:8000/credit_ticket/{código do ticket} -> Rota GET para a consulta do status de crédito através do ticket gerado, basta colocar o ticket no parâmetro da url.

## Exemplo de dado semi-estruturado para realizar a solicitação de crédito
```json
{
	"name":"matheus",
	"cpf": "11122233344",
	"birth_date": "1999-05-31",
	"value_credit": "50000"
}
```

### Resposta da requisição
É retornado o ticket da solitação do usuário para que possa consultar o status da solicitação.
```json
{
  "ticket": "fd7011f6-964e-4bb6-9dd2-34e554703ace"
}
```
Dependendo dos dados enviados na solicitação de crédito, se estiverem inválidos ou com alguma discrepância. É retornado uma lista de erros.
```json
{
	"name":"matheus",
	"cpf": "0000000000000000000",
	"birth_date": "1999-05-31",
	"value_credit": "-1"
}
```
### Resposta da requisição
```json
{
  "Errors": [
    "CPF inválido",
    "Valor do crédito está inválido"
  ]
}

```

## Consultando o status da solicitação
Para consultar o status basta colocar o valor do ticket na url, exemplo: http://localhost:8000/credit_ticket/fd7011f6-964e-4bb6-9dd2-34e554703ace

### Resposta da requisição
```json
{
  "Status": "Aprovado"
}
```

## Explicando o assincronismo na validação
Na hora que é feito o POST pra o pedido de crédito, imediatamente é gerado um ticket, os dados da requisição são inserido no banco de dados junto atributo `status` o seu valor inicia com "Em avaliação" e após isso é retornado como resposta o ticket da solicitação. Em meio a esse processo é disparado uma thread assincrona que irá enviar os dados para serem validados em outro sistema, isso dá uma grande vantagem pois não vai ser preciso esperar a resposta do servidor de validação para poder retornar o ticket para o usuário. Logo quando a resposta do sistema validação é retornada, a resposta da solicitação de crédito é atualizada no banco de dados. 

## Logging implementado
Nesse desafio pela primeira vez que mexir com logging, achei muito interessante, pois podemos registrar as ações do sistema e ainda definir os quais tipos logs queremos, para assim ter o controle do que acontece com o sistema e também registrar as ações de cada requisição realizada.

![Alt text](./images_readme/logging.PNG?raw=true "Optional Title")

## Rodando a aplicação no ambiente docker
Para rodar o sistema, basta abrir o terminal da raiz do projeto e executar o comando `docker-compose up`. Esse comando irá subir 3 containers: 
- Postgres
- Sistema de validação
- Api
  
Após subir todos os containers, a aplicação estará disponivel http://localhost:8000

## Usando o insomnia para fazer requições para a Api
Para fazer as requisições para Api, o usei o programa chamado insomnia. Muito bom para fazer as requisições HTTP.

![Alt text](./images_readme/post_credit.PNG?raw=true "Optional Title")

![Alt text](./images_readme/get_status.PNG?raw=true "Optional Title")
