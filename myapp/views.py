from django.shortcuts import render
from .models import Account, DepositTransaction, WithdrawTransaction
from django.http import HttpResponse
people = Account.objects.all()
transactionsOut = WithdrawTransaction.objects.all()
transactionsIn = DepositTransaction.objects.all()

def index(request):
    return render(request, "home.html", {"accounts": people })
    
def banking(request):
    
    return render(request, "banking.html", {"accounts": people })

def depositing(request):
    return render(request, "deposit.html", {"deposits": transactionsIn})
    