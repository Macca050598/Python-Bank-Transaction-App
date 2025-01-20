from django.db import models

class Account(models.Model):
    account_id = models.BigIntegerField(primary_key=True)
    account_name = models.CharField(max_length=200)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)  # For monetary values
    account_creation_time = models.DateTimeField("date created", auto_now_add=True)

    def __str__(self):
        return self.account_name

class DepositTransaction(models.Model):
    deposit_id = models.BigIntegerField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="deposits")
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deposit_creation_time = models.DateTimeField("date created", auto_now_add=True)

    def __str__(self):
        return f"Deposit {self.deposit_id} for {self.account.account_name}"

class WithdrawTransaction(models.Model):
    withdraw_id = models.BigIntegerField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="withdrawals")
    withdraw_amount = models.DecimalField(max_digits=10, decimal_places=2)
    withdraw_creation_time = models.DateTimeField("date created", auto_now_add=True)

    def __str__(self):
        return f"Withdraw {self.withdraw_id} for {self.account.account_name}"
