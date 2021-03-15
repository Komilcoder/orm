from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id','_id','request_id','amount','account','state','date')
    list_display_links = ('id')


admin.site.register(Transaction,TransactionAdmin)    