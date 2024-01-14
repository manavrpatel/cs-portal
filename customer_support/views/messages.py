from rest_framework import generics
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from customer_support.serializers.messages import MessageCreateSerializer
from customer_support.models.messages import Message
from customer_support.models.tickets import Ticket
from django.core.exceptions import ValidationError

class MessageCreateAPI(APIView):
    def post(self, request, *args, **kwargs):
        message_info= {
            'senderID': request.data.get('senderID'),
            'ticketID': request.data.get('ticketID'),
            'content': request.data.get('content')
        }
        serializer = MessageCreateSerializer(data=message_info)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse({"message": "bad request"}, status=status.HTTP_400_BAD_REQUEST)


class MessagesGetAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ticket_id = request.GET.get('ticket_id')
            ticket_info=Ticket.objects.filter(ticketID=ticket_id)
            ticket_info = list((ticket_info).values('title', 'status'))
            messages = list(Message.objects.filter(ticketID=ticket_id).values('senderID', 'content', 'timestamp').order_by('timestamp'))
            response = {
                'ticketID': ticket_id,
                'title': ticket_info[0]['title'],
                'status': ticket_info[0]['status'],
                'messages': messages
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'message': f"Error in getting messages: {e}"}, status=500)