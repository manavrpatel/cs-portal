from rest_framework import generics
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from customer_support.serializers.tickets import TicketCreateSerializer, TicketUpdateSerializer
from customer_support.models.tickets import Ticket

class TicketCreateAPI(APIView):
    def post(self, request, *args, **kwargs):

        ticket_info= {
            'customerID': request.data.get('userID'),
            'title': request.data.get('title')
        }

        serializer = TicketCreateSerializer(data=ticket_info)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
class TicketDetailsAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            ticketID = pk
            ticket_info = Ticket.objects.filter(ticketID=ticketID)
            serializer = TicketCreateSerializer(ticket_info, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'message': f"Error in getting ticket-details: {e}"}, status=500)
    
class TicketUpdateAPI(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketUpdateSerializer