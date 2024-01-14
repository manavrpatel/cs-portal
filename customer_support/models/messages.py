from uuid import uuid4
from django.db import models
from users.models import User
from customer_support.models.tickets import Ticket

class Message((models.Model)):
    messageID =  models.UUIDField(primary_key=True, default=uuid4)
    content = models.TextField(max_length=1000, null=False)
    senderID = models.ForeignKey(User, on_delete=models.CASCADE)
    ticketID = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)