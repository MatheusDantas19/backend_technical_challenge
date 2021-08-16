from django.contrib import admin
from api.models import RequisitionCredit

# Register your models here.

class RequisitionCreditAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'birth_date', 'value_credit', 'status')
    list_display_links = ('name', 'cpf', 'status')
    list_per_page = 30

admin.site.register(RequisitionCredit, RequisitionCreditAdmin)

