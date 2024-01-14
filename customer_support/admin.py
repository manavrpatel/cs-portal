from django.contrib import admin
from customer_support.models.tickets import Ticket
from customer_support.models.messages import Message

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Message)
