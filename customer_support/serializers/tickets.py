from rest_framework.serializers import ModelSerializer
from customer_support.models.tickets import Ticket

class TicketCreateSerializer(ModelSerializer):
    class Meta:
        model=Ticket
        fields='__all__'
        extra_kwargs={'ticketID': {'required': False}}

class TicketUpdateSerializer(ModelSerializer):
    class Meta:
        model=Ticket
        fields = ['status']