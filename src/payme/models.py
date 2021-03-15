from django.db import models
from django.contrib.auth import get_user_model


class UserPayment(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=255)
    time = models.DateTimeField()
    paid_time = models.DateTimeField()
    amount = models.DecimalField(decimal_places=2,max_digits=7)
    merchant_id = models.CharField(max_length=100)
    merchant_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}{}'.format(self.user, self.payment_id)