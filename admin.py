from django.contrib import admin
from .models import MemberProfile, Transaction,Loan,LoanPayment,Organization
# Register your models here.
admin.site.register([MemberProfile, Transaction,Loan,LoanPayment,Organization])
