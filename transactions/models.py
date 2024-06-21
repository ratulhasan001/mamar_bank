from django.db import models
from accounts.models import UserBankAccount
# Create your models here.
from .constants import TRANSACTION_TYPE
from django.contrib.auth.models import User

class Transaction(models.Model):
    account = models.ForeignKey(UserBankAccount, related_name = 'transactions', on_delete = models.CASCADE) # ekjon user er multiple transactions hote pare
    
    amount = models.DecimalField(decimal_places=2, max_digits = 12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits = 12)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False) 
    
    class Meta:
        ordering = ['timestamp'] 
        
class Transfer(models.Model):
    sender = models.ForeignKey(UserBankAccount, related_name="transfer_sender", on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name="transfer_reciever", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    
    class Meta:
        ordering = ['timestamp']
        
class Bank(models.Model):
    name = models.CharField(unique=True, max_length=255)
    is_bankrupt = models.BooleanField(default=False)