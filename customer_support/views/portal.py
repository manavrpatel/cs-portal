from django.shortcuts import render
from customer_support.models.tickets import Ticket
from customer_support.models.messages import Message
from users.models import User

def portal(request, ticket_id):
    ticket = Ticket.objects.get(ticketID=ticket_id)
    messages = Message.objects.filter(ticketID=ticket_id)[0:25]
    username = request.COOKIES.get('username')
    return render(request, 'customer_support/chat.html', {'user':username, 'ticket': ticket, 'messages': messages})


def home(request):
    tickets = Ticket.objects.all()
    user = request.COOKIES.get('username')
    author_id = User.objects.filter(username=user).values('userID', 'role')
    role = author_id[0]['role']
    if role=='AGENT':
        tickets = Ticket.objects.all()
    else:
        tickets = Ticket.objects.filter(customerID=author_id[0]['userID'])
    return render(request, 'customer_support/portal.html', {'tickets':tickets, 'user':user})
