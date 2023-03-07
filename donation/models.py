from django.db import models

# Create your models here.

PAYMENT_CHOICES = [('Payme', 'Payme'),
                   ('Oson', 'Oson'),
                   ('Click', 'Click')
                   ]


class Donation(models.Model):
    full_name = models.CharField(max_length=90)
    donation_amount = models.DecimalField(default=0, max_digits=12, decimal_places=3)
    payment_type = models.CharField(max_length=30, choices=PAYMENT_CHOICES)

    def __str__(self):
        return str(self.donation_amount)


