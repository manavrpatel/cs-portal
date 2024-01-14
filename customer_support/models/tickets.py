from uuid import uuid4
from django.db import models
from users.models import User
from enum import Enum

class TicketStatus(Enum):
    # resolve, unresolved
    resolved="RESOLVED"
    unresolved="UNRESOLVED"

class Ticket((models.Model)):
    TICKETS_STATUS = [
        (TicketStatus.resolved.value, 'RESOLVED'),
        (TicketStatus.unresolved.value, 'UNRESOLVED')
    ]
    ticketID =  models.UUIDField(primary_key=True, default=uuid4)
    title = models.TextField(max_length=100, null=False)
    customerID = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=TICKETS_STATUS, default="UNRESOLVED")

    def __str__(self):
        return self.title