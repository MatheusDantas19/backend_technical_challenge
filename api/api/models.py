from django.db import models

# Create your models here.
class RequisitionCredit(models.Model):
    ticket_id = models.TextField(primary_key=True)
    name = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()
    value_credit = models.FloatField()
    status = models.CharField(max_length=20, default='Em Avaliação')

def __str__(self):
    return self.name
