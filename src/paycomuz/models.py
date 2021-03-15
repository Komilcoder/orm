from django.db import models



class Transaction(models.Model):
    PROCESSING = 'processing'
    SUCCESS = 'success'
    FAILED = 'failed'
    CANCELED = 'canceled'
    STATUS = (
        (PROCESSING, 'processing'),
        (SUCCESS, 'success'),
        (FAILED, 'failed'),
        (CANCELED, 'canceled')
    )

    _id = models.CharField(max_length=255)
    request_id = models.IntegerField()
    order_key = models.CharField(max_length=255,null=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    state = models.IntegerField(blank=True,null=True)
    status = models.CharField(max_lenght=55,default='processing',choices=STATUS)
    perform_datetime = models.CharField(max_length=255,null=True)
    cancel_datetime = models.CharField(null=True,max_length=255)
    created_datetime = models.CharField(null=True,max_length=255)
    reason = models.IntegerField()

    def __str__(self):
        return str(self.id)