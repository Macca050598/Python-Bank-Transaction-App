from django.shortcuts import render
from .models import Account, DepositTransaction, WithdrawTransaction
from django.http import HttpResponse


def index(request):
    return render(request, "home.html")
    
def banking(request):
    people = Account.objects.all()
    transactionsIn = DepositTransaction.objects.all()
    transactionsOut = WithdrawTransaction.objects.all()
    return render(request, "banking.html", {"accounts": people })
    