from django.db import models
from django.contrib.auth.models import User


class Webpage(models.Model):
    # Your fields here
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    nid_number = models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.user.username)  


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('DEPOSIT', 'Deposit'),
        ('CASH_OUT', 'Cash Out'),
    )

    member = models.ForeignKey(MemberProfile, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        user = self.member.user if isinstance(self.member, MemberProfile) else None
        return f"{self.transaction_type} of {self.amount} by {user.username if user else 'Unknown'}"


class Loan(models.Model):
    LOAN_TYPES = (
        ('PERSONAL', 'Personal Loan'),
        ('HOME', 'Home Loan'),
        ('EDUCATIONAL', 'Educational Loan'),
        ('AGRICULTURE', 'Agriculture Loan'),
    )

    member = models.ForeignKey(MemberProfile, on_delete=models.CASCADE)
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.FloatField()
    duration_months = models.PositiveIntegerField()
    start_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        user = self.member.user if isinstance(self.member, MemberProfile) else None
        return f"{self.loan_type} Loan for {user.username if user else 'Unknown'}"


class LoanPayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"Payment of {self.amount_paid} for Loan ID {str(self.loan.id)}"


class Organization(models.Model):
    name = models.CharField(max_length=100)


